from rest_framework import serializers
from market.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    article_name = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super(ArticleSerializer, self).to_representation(instance)
        rep['owner'] = instance.owner.username
        rep['category'] = instance.category.name
        rep['guraantee'] = instance.guraantee.guarantee_length
        rep['color'] = instance.color.color
        return rep

