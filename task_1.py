# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та
# сортує в піддиректорії, назви яких базуються на розширенні файлів.

import os
import shutil
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Copy and sort files by extension.')
    parser.add_argument('source', type=str, help='Path to the source directory')
    parser.add_argument('destination', type=str, nargs='?', default='dist',
                        help='Path to the destination directory (default: dist)')
    return parser.parse_args()


def copy_and_sort_files(src_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                copy_and_sort_files(src_path, dest_dir)
            else:
                # отримати розширення файлу без крапки
                file_extension = os.path.splitext(item)[1][1:]
                if not file_extension:
                    file_extension = 'no_extension'

                ext_dir = os.path.join(dest_dir, file_extension)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)

                dest_path = os.path.join(ext_dir, item)
                shutil.copy2(src_path, dest_path)
                print(f"Copied {src_path} to {dest_path}")

    except Exception as e:
        print(f"Error processing {src_dir}: {e}")


def main():
    args = parse_arguments()
    source_dir = os.path.abspath(args.source)
    destination_dir = os.path.abspath(args.destination)

    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return

    copy_and_sort_files(source_dir, destination_dir)


if __name__ == "__main__":
    main()