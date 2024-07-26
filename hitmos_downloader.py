from grabber import Grabber
import argparse

tag = 'a'
class_ = 'track__download-btn ___adv-binded ___adv-yandex-browser ___adv-yandex-browser-download ___adv-download'


def arg_parse():
    parser = argparse.ArgumentParser(
        description='Download all music from https://rus.hitmotop.com/')
    parser.add_argument(
        'url', type=str, help='url to download -> https://rus.hitmotop.com/genre/6'
    )
    parser.add_argument(
        'download_folder', type=str, help='Directory for storing save files -> downloads/'
    )
    return parser.parse_args()


def main():
    args = arg_parse()
    grab = Grabber(args.url)
    res = grab.get_element('a', class_='track__download-btn', attr_='href')
    for link in res:
        grab.download(link, link[44:], args.download_folder)


if __name__ == "__main__":
    main()
