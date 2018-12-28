from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
def run_index():
    return render_template('index.html')

@app.route('/api/123123')
def hello_world():
    # import datetime
    targetDay = datetime.datetime.now().date()  #将输入的日期格式化成标准的日期
    dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  #减去上一年最后一天
    totalCount = datetime.date(targetDay.year, 12, 31) - datetime.date(targetDay.year - 1, 12, 31)  #减去上一年最后一天
    # print(dayCount.days, totalCount.days, dayCount.days/totalCount.days)
    # return '22'
    return str(dayCount.days/totalCount.days*100)
 
if __name__ == '__main__':
    app.run(debug=True)