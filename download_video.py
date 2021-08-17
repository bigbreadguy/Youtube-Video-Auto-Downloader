from util import *
import secret
import glob
import tqdm

if __name__ == "__main__":
    DEVELOPER_KEY = secret.API_KEY
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    
    cwd = os.getcwd()
    result_dir = os.path.join(cwd, "result")
    save_dir = os.path.join(result_dir, "video_url")
    load_dir = os.path.join(result_dir, "search")
    download_dir = os.path.join(cwd, "downloads")

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    searched = glob.glob(os.path.join(load_dir, "*.json"))
    search_results = dict()
    for s_path in searched:
        with open(s_path, 'r', encoding = "UTF-8-SIG") as file_load:
            s_dict = json.load(file_load)
            search_results.update(s_dict)

    quo = len(search_results) // 50
    rem = len(search_results) % 50
    
    print(f"Loading Total {len(search_results)} Videos")

    ids_in_chunk = []
    for i in range(quo+1):
        from_ = i * 50
        to_ = i * 50 + rem if i==quo else (i + 1) * 50
        print(f"Processing Video No.{from_ + 1} to No.{to_}")
        ids = ",".join(list(search_results.values())[from_:to_])
        ids_in_chunk.append(ids)

    argparser.add_argument("--id", help="Video ID", default=ids_in_chunk[0])
    argparser.add_argument("--max-results", help="Max results", default=50)
    args = argparser.parse_args()

    parser = URLParser()
    
    for i in range(quo+1):
        args.id = ids_in_chunk[i]
        try:
            videos_results = youtube_video(args, parser, DEVELOPER_KEY)
            with open(os.path.join(save_dir, f"videos_results_{i}.json"), 'w', encoding = "UTF-8-SIG") as file_out:
                json.dump(videos_results, file_out, ensure_ascii=False)

            for v in tqdm.tqdm(videos_results.values()):
                url = v["url"]
                download(url, download_dir)

        except HttpError as e:
            print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))