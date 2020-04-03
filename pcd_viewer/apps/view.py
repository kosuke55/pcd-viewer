import argparse
import numpy as np
import open3d as o3d
import os


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input', '-i', type=str,
                        help='Input pcd filename', required=True)
    parser.add_argument('--channel', '-c', type=int,
                        help='Channel of pcd data.',
                        default=4)
    args = parser.parse_args()
    root, ext = os.path.splitext(args.input)

    if 'bin' in ext:
        points_flatten = np.fromfile(args.input, dtype=np.float32)
        points = points_flatten.reshape(-1, args.channel)
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points[:, :3])

    else:
        pcd = o3d.io.read_point_cloud(args.input)

    o3d.visualization.draw_geometries([pcd])


if __name__ == '__main__':
    main()
