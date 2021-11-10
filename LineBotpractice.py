
from linebot import LineBotApi
from linebot.models import LocationSendMessage
from linebot.exceptions import LineBotApiError
from linebot.models import  CarouselTemplate, CarouselColumn, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction,TextSendMessage, ImageSendMessage,TemplateSendMessage



CHANNEL_ACCESS_TOKEN = "***********iX3Z863Cz9MvSbLi6zMtK0heTr+Bhq2Lc4Z9EV7CRk542Kuc6nv/Mr1kpz/w6tw5AdB04t89/1O/w1cDnyilFU="
to = "*******4ef161153cb5d0a0"


def get_room_member_ids(self, room_id, start=None, timeout=None):
 member_ids_res = line_bot_api.get_room_member_ids(room_id)

 print(member_ids_res.member_ids)
 print(member_ids_res.next)
# return member_ids_res
#文字訊息
try:
    LineBotApi.push_message(to, TextSendMessage("000"))
except LineBotApiError as e:
    # error handle
    raise e
    

button_template_message =ButtonsTemplate(
                            thumbnail_image_url="https://scontent.ftpe7-1.fna.fbcdn.net/v/t1.0-9/40307916_1971455449585364_8954308660931067904_n.jpg?_nc_fx=ftpe7-3&_nc_cat=0&oh=f44de9c2910db3a4f8b09741e7aea91f&oe=5C008CEB",
                            title='台中五金商圈Menu', 
                            text='請選擇',
                            ratio="1.51:1",
                            image_size="cover",
                            actions=[
#                                PostbackTemplateAction 點擊選項後，
#                                 除了文字會顯示在聊天室中，
#                                 還回傳data中的資料，可
#                                 此類透過 Postback event 處理。
                                PostbackTemplateAction(
                                    label='商圈店家瀏覽', 
                                    text='postback text',
                                    data='action=buy&itemid=1'
                                ),
                                MessageTemplateAction(
                                    label='商品類別瀏覽', text='message text'
                                    #label='message會回傳text文字', text='message text'
                                ),
                                URITemplateAction(
                                    label='與我聊聊天', uri='http://www.xiaosean.website/'
                                )
                            ]
                        )
try:
#     alt_text 因template只能夠在手機上顯示，因此在PC版會使用alt_Text替代
     line_bot_api.push_message(to,TemplateSendMessage(alt_text="Template Example", template=button_template_message))
except LineBotApiError as e:
    # error handle
     raise e  
image_url_1 = "https://scontent.ftpe7-4.fna.fbcdn.net/v/t1.0-9/40244707_1971485689582340_2106677949699719168_n.jpg?_nc_fx=ftpe7-3&_nc_cat=0&oh=40540a3736db48e078103197a67ae4eb&oe=5BEEEEFC"
image_url_2 = "https://scontent.ftpe7-1.fna.fbcdn.net/v/t1.0-9/40253699_1971490392915203_2467305875140771840_o.jpg?_nc_fx=ftpe7-3&_nc_cat=0&oh=4dfb474ec83cdd02c8017f9e15407995&oe=5BFCADF9"
click_link_1 = "https://www.facebook.com/ntustcc"
click_link_2 = "https://www.facebook.com/ntustcc"
carousel_template = template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=image_url_1,
                    title='岱旺有限公司',
                    text='套筒板手組',
                    actions=[
                        PostbackTemplateAction(
                            label='店家位置',
                            text='postback text1',
                            data='result=1'
                        ),
                        MessageTemplateAction(
                            label='加入好友',
                            text='message text1'
                        ),
                        URITemplateAction(
                            label='店家網頁',
                            uri=click_link_1
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=image_url_2,
                    title='元達切削刀具',
                    text='切削工具',
                    actions=[
                        PostbackTemplateAction(
                            label='店家位置',
                            text='postback text1',
                            data='result=1'
                        ),
                        MessageTemplateAction(
                            label='加入好友',
                            text='message text1'
                        ),
                        URITemplateAction(
                            label='店家網頁',
                            uri=click_link_1
                        )
                    ]
                )]
            )
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

try:
#     alt_text 因template只能夠在手機上顯示，因此在PC版會使用alt_Text替代
  line_bot_api.push_message(to, TemplateSendMessage(alt_text="Carousel Template Example", template=carousel_template))
except LineBotApiError as e:
    # error handle
     raise e
    
title = "岱旺有限公司"
address = "406台中市太平區永平路三段5號"
latitude = 24.128078
longitude = 120.708268
try:
    line_bot_api.push_message(to, LocationSendMessage(title=title,
                                                      address=address,
                                                      latitude=latitude,
                                                      longitude=longitude))
except LineBotApiError as e:
    # error handle
     raise e
                     
