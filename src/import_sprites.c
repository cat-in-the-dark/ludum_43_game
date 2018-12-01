#include <jvcr_ecm_01/import_sprites.h>
#include <png.h>
#include <stdio.h>
#include <stdlib.h>
#include <jvcr_ecm_01/ram.h>

typedef void (*Filler)(Jvcr *, const png_byte *, u32, u32);

static void fill_4bit(Jvcr *machine, const png_byte *row, u32 x, u32 y) {
  png_byte pyxel = row[x];
  byte low = (byte) (pyxel & 0x0F);
  byte high = (byte) ((pyxel >> 4) & 0x0F);

//  printf("%2d %2d ", high, low);
  jvcr_poke_sprite(machine->ram, 2 * x, y, high);
  jvcr_poke_sprite(machine->ram, 2 * x + 1, y, low);
}

static void fill_8bit(Jvcr *machine, const png_byte *row, u32 x, u32 y) {
  png_byte pyxel = row[x];
//  printf("%2d ", pyxel);
  jvcr_poke_sprite(machine->ram, x, y, pyxel);
}

void import_sprites(Jvcr *machine, const char *path, ptr_t offset) {
  FILE *file = fopen(path, "rb");
  if (file == NULL) {
    perror("File opening failed");
    exit(-1);
  }
  unsigned char header[8];
  fread(header, 1, 8, file);
  if (png_sig_cmp(header, 0, 8)) {
    printf("File %s is not recognized as a PNG file", path);
    exit(-1);
  }
  png_structp png = png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
  if (png == NULL) {
    perror("png_create_read_struct failed");
    exit(-1);
  }
  png_infop info = png_create_info_struct(png);
  if (info == NULL) {
    perror("png_create_info_struct failed");
    exit(-1);
  }
  if (setjmp(png_jmpbuf(png))) {
    perror("[read_png_file] Error during init_io");
    exit(-1);
  }
  png_init_io(png, file);
  png_set_sig_bytes(png, 8);
  png_read_info(png, info);

  unsigned long width = png_get_image_width(png, info);
  unsigned long height = png_get_image_height(png, info);
  png_byte color_type = png_get_color_type(png, info);
  png_byte bit_depth = png_get_bit_depth(png, info);

  printf("width=%lu height=%lu color_type=%d bit_depth=%d\n", width, height, color_type, bit_depth);

  if (color_type != PNG_COLOR_TYPE_PALETTE) {
    printf("Image should be with palette color type\n");
    exit(-1);
  }

  Filler filler;
  if (bit_depth == 4) {
    filler = &fill_4bit;
  } else if (bit_depth == 8) {
    filler = &fill_8bit;
  } else {
    printf("Image should be with bit_depth=4 or 8\n");
    exit(-1);
  }

  png_bytepp row_pointers = (png_bytep *) malloc(sizeof(png_bytep) * height);
  size_t row_size = png_get_rowbytes(png, info);
  printf("row_size = %lu\n", row_size);
  for (png_uint_32 y = 0; y < height; y++) {
    row_pointers[y] = (png_byte *) malloc(row_size);
    for (png_uint_32 x = 0; x < row_size; x++) {
      row_pointers[y][x] = 0;
    }
  }
  png_read_image(png, row_pointers);

  for (u32 y = 0; y < height; y++) {
    png_bytep row = row_pointers[y];
    for (u32 x = 0; x < row_size; x++) {
      filler(machine, row, x, y);
    }
  }

  printf("SUCCESS. File was read %s\n", path);
  for (png_uint_32 y = 0; y < height; y++) {
    free(row_pointers[y]);
  }
  free(row_pointers);
  fclose(file);
}

