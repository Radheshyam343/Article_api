
from rest_framework import serializers
from .models import Article

# model class serializers
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields =  ['id','title','author']

