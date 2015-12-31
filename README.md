S3 auto-uploader: watch directories and upload new files to S3
==============================================================

This program will watch a given directory and upload any new files that appear in it to [AWS S3](https://aws.amazon.com/s3/), deleting the local copies afterwards.

The script will only upload files created after it has started running.

For the upload to work, certain environment variables must be set:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `S3_BUCKET`

The bucket specified in the latter should already be created.


Running
-------

If you have [Docker](https://docker.com/), you can run this program as follows:

```sh
export AWS_ACCESS_KEY_ID=…
export AWS_SECRET_ACCESS_KEY=…
export S3_BUCKET=…
export TARGET_DIR=/path/to/directory/you/want/to/watch
make
```

(You can also modify the Docker command in the Makefile to run in the background.)

If you don't, you can also execute the `run` script directly, after installing dependencies:

```sh
export AWS_ACCESS_KEY_ID=…
export AWS_SECRET_ACCESS_KEY=…
export S3_BUCKET=…
pip install -r requirements.txt
./run /path/to/directory/you/want/to/watch
```

If you don't specify a target directory, the current working directory will be the one watched for new files.
