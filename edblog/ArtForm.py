from django import forms


# 添加文章的表单
class AddArtForm(forms.Form):
    title = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'required':'文章简述必填',
                                'min_length':'文章描述不能少于2'
                            })
    describe = forms.CharField(min_length=2,required=True,
                           error_messages={
                               'required': '文章简述必填',
                               'min_length': '文章描述不能少于2'
                           })
    content = forms.CharField(required=True,
                           error_messages={
                               'required': '文章简述必填',
                           })
    # icon = forms.ImageField(required=True,error_messages={
    #     'required': '首图必填'
    # })


# 修改文章的表单
class EditArtForm(forms.Form):
    title = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'required': '标题必填',
                                'min_length': '文章title不能少于2'
                            })
    describe = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'required': '描述必填',
                                'min_length': '文章描述不能少于2'
                            })
    content = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'required': '内容必填',
                                'min_length': '文章内容不能少于2'
                            })








