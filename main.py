# coding:utf-8
import re
import sys
import time

from workflow import Workflow3

reload(sys)
sys.setdefaultencoding('utf8')

pattern_ts_sec = re.compile('1[6789]\d{7}|1[6789]\d{10}')
pattern_ts_format = re.compile('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')


def main(wf):
    query = wf.args[0]
    if query == 'now':
        cur_time = time.time()
        time_tuple = time.localtime(cur_time)
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
        wf.add_item(title=int(cur_time),
                    subtitle='时间戳',
                    arg=int(cur_time),
                    valid=True)
        wf.add_item(title=int(cur_time * 1000),
                    subtitle='毫秒时间戳',
                    arg=int(cur_time * 1000),
                    valid=True)
        wf.add_item(title=formatted_time,
                    subtitle='格式化时间',
                    arg=formatted_time,
                    valid=True)
    elif re.match(pattern_ts_sec, query):
        if len(query) == 13:
            query = str(query[0:-3])
        query = float(query)
        cur_time = time.localtime(query)
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", cur_time)
        wf.add_item(title=formatted_time,
                    subtitle='格式化时间',
                    arg=formatted_time,
                    valid=True)
    elif re.match(pattern_ts_format, query):
        cur_time = time.strptime(query, '%Y-%m-%d %H:%M:%S')
        ts = time.mktime(cur_time)
        wf.add_item(title=ts,
                    subtitle='时间戳',
                    arg=ts,
                    valid=True)
    else:
        wf.add_item(title='请输入时间相关内容',
                    subtitle='请输入时间相关内容')

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
