# encoding: utf-8

"""
通用ＵＲＬ类,知乎官方ＵＲＬ接口地址
这里加一句测试代码
"""


class URL(object):
    host = "https://www.zhihu.com"

    # 登录
    @staticmethod
    def login():
        return URL.host + "/login/email"

    # 私信
    @staticmethod
    def message():
        return URL.host + "/api/v4/messages"

    # 验证码
    @staticmethod
    def captcha(timestamp):
        return URL.host + "/captcha.gif?r={timestamp}&type=login".format(timestamp=timestamp)

    # 首页
    @staticmethod
    def index():
        return URL.host + ""

    # 用户信息
    @staticmethod
    def profile(user_slug):
        return URL.host + "/api/v4/members/{user_slug}".format(user_slug=user_slug)

    # 关注用户
    @staticmethod
    def follow(user_slug):
        return URL.host + "/api/v4/members/{user_slug}/followers".format(user_slug=user_slug)

    # 赞同/反对/中立
    @staticmethod
    def vote_up(answer_id):
        return URL.host + "/api/v4/answers/{id}/voters".format(id=answer_id)
