"""任务2：推算几天后的日期"""
import datetime


def inputDate():
    inDate=input("输入日期，如(20200808)：")
    # inDate=inDate.strip()
    date_str=inDate[0:4]+"-"+inDate[4:6]+"-"+inDate[6:]
    return datetime.datetime.strptime(date_str,"%Y-%m-%d")

if __name__ == '__main__':
    sDate=inputDate()

    in_num=int(input("输入间隔天数"))
    f=sDate+datetime.timedelta(days=in_num)
    print("推算日期是：",str(f).split(" ")[0])