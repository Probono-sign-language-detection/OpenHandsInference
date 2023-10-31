import boto3
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

def download_from_s3(s3_url="https://bitamin-video-storage.s3.amazonaws.com/video/tmp6_pj3avh.mov"):
    """
    bucket_name: S3 버킷 이름
    s3_key: S3에서 다운로드할 파일의 키 (경로 포함)
    download_path: 파일을 저장할 로컬 경로
    """
    ## TODO: 1. 경로 전부 환경변수로 / url 다운로드 파일 parseing하게

    try:
        load_dotenv()

        s3_client = boto3.client('s3',
                                aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                                aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY_SECRET'))

        # 파일 다운로드
        """
        버킷네임, s3_key는 s3_url에 있음
        """
        parsed = urlparse(url=s3_url, allow_fragments=False)
        bucket_name = parsed.netloc.split(".s3.amazonaws.com")[0]
        s3_key = parsed.path.lstrip("/")
        
        download_path = r"C:\Users\JeongSeongYun\Desktop\OpenHands\OHTest\test_videos\s3_test.mov"

        s3_client.download_file(bucket_name, s3_key, download_path)
        print(f"Downloaded {s3_key} from {bucket_name} to {download_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Downloading Video from S3...")

    download_from_s3(s3_url="https://bitamin-video-storage.s3.amazonaws.com/video/tmp6_pj3avh.mov")
    print(f"Done!")

