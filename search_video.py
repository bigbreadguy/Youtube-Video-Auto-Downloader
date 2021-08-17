from util import *
import secret
import tqdm

def try_search(args, DEVELOPER_KEY):
    try:
        search_results = youtube_search(args, DEVELOPER_KEY)
        cwd = os.getcwd()
        result_dir = os.path.join(cwd, "result")
        save_dir = os.path.join(result_dir, "search")
        if not os.path.exists(result_dir):
            os.mkdir(result_dir)
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        with open(os.path.join(save_dir, f"search_results_{args.q}.json"), 'w', encoding = "UTF-8-SIG") as file_out:
            json.dump(search_results, file_out, ensure_ascii=False)

    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))

if __name__ == "__main__":
    DEVELOPER_KEY = secret.API_KEY

    queries = ["해외 반응", "외국인 반응", "외국인 리액션"]

    argparser.add_argument("--published-after", help="Start Date", default="2020-08-14T00:00:00Z")
    argparser.add_argument("--q", help="Search term", default=queries[0])
    argparser.add_argument("--type", help="Type", default="video")
    argparser.add_argument("--max-results", help="Max results", default=50)
    argparser.add_argument("--page-token", help="nextPageToken or prevPageToken", default="nextPageToken")
    args = argparser.parse_args()

    for query_ in tqdm.tqdm(queries):
        args.q = query_
        try_search(args, DEVELOPER_KEY)
