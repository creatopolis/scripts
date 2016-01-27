#!/usr/bin/python
# This is a one-off script that is run to tag the latest backup as the last known
# "good" state of the server.
# Author: Alvin Lin (alvin.lin.dev@gmail.com)

import os
import sys
import datetime

import backup

CONFIG_FILENAME = "backup_config.json"

def main():
  """
  Main function, reads the config and updates the last known good state backup.
  """
  config = backup.get_config()
  backups = sorted(backup.list_files_all("/home/omgimanerd/minecraft/backups"))

  creative_backups = filter(
    lambda x: x.find("creative_backup") + 1, backups)
  creative_freebuild_backups = filter(
    lambda x: x.find("creative_freebuild") + 1, backups)
  plugins_backups = filter(
    lambda x: x.find("plugins_backup") + 1, backups)

  for b in sorted(creative_backups):
    print b

if __name__ == "__main__":
  main()
