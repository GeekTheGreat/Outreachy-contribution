#include <glusterfs/api/glfs.h>
#include<stdio.h>
// This program creates a file and writes to it.

int main (int argc, char** argv) {
  glfs_t *fs = NULL;
  glfs_fd_t *fd = NULL;
  int ret;
  char *filename = "testfile";

  fs  = glfs_new ("replicatedVol");
  ret = glfs_set_volfile_server (fs, "tcp", "10.135.159.177", 24007);
  ret = glfs_init (fs);
  fd  = glfs_creat (fs, filename, O_RDWR, 0644); 
  ret = glfs_write (fd, "hello world!", 15, 0);
  glfs_close (fd);
  return 0;
}

