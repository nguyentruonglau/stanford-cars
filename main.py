from shutil import copyfile
import sys
import argparse
import os
import scipy.io


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, default='cars_test')
    parser.add_argument('--label_path', type=str, default='cars_test_annos_withlabels.mat')

    parser.add_argument('--output_dir', type=str, default='./dataset/test')
    return parser.parse_args(args)


def read_mat_file(file_path):
    """Read mat files
    """
    data = scipy.io.loadmat(file_path)
    return data


def main(args):
    data = read_mat_file(args.label_path)

    for i in range(len(data['annotations'][0])):

        path = data['annotations'][0][i][-1][0]
        label = str(data['annotations'][0][i][-2][0][0])

        try:
            src_path = os.path.join(args.input_dir, path)
            dst_path = os.path.join(args.output_dir, label, path)

            os.makedirs(os.path.join(args.output_dir, label), exist_ok=True)

            copyfile(src_path, dst_path)
        except:
            print('[INFOR]: Error at {}'.format(src_path))


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    
    print('\ninput_dir=', args.input_dir)
    print('label_path=', args.label_path)
    print('output_dir=', args.output_dir, '\n')

    print('[INFOR]: Start...')
    main(args)
    print('[INFOR]: End')