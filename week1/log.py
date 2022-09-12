import re


def logs():
    with open("logdata.txt", "r") as file:
        result = []
        for line in file.readlines():
            web_dirt = {'host': '', 'user_name': '', 'time': '', 'request': ''}
            a = re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}', line)
            web_dirt['host'] = a[0]
            b = re.findall('(?<= - ).+(?= \[)', line)
            web_dirt['user_name'] = b[0]
            c = re.findall('(?<=\[).+(?=\])', line)
            web_dirt['time'] = c[0]
            d = re.findall('(?<=\").+(?=\")', line)
            web_dirt['request'] = d[0]
            #             print("a")
            result.append(web_dirt)
        return result


if __name__ == '__main__':
    logs()
