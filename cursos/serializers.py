from rest_framework import serializers
from django.db.models import Avg
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'ativo'
        )

    # o padrão do Serializer exige que o método de validação tenha o nome validade + campo se quer validar
    def validate_avaliacao(self, valor):  # 1, 2, 3, 4, 5
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5.')


class CursoSerializer(serializers.ModelSerializer):
    # Primeira abordagem com nested relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Segunda abordagem com HyperLinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    """"
    Com essa segunda abordagem, avaliacoes será listada com os links das avaliações e não o conteúdo de cada avaliação, diminuindo o payload.
    Ainda assim haverá um processamento. Pense que um curso poderia ter 100k de avaliações.
    "avaliacoes": [
        "http://localhost:8000/api/v2/avaliacoes/3/"
    ]
    """
    # terceira abordagem com Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)



    # aqui estou criando um atributo que será um método que irá retornar o valor dele. O nome do método deve ser
    # get_nome_do_atributo.
    media_avaliacoes = serializers.SerializerMethodField()

    def get_media_avaliacoes(self, obj):
        # aqui estou acessando a propriedade avaliacoes do model Curso. A partir desse campo
        # é utilizada a função de agregação Avg sobre o campo avaliacao que vem do model Avaliacao.
        # No final do cálculo é provido um campo avaliacao__avg, que então é capturado.
        # Aqui seria um problema se tivesse muitas avaliações e muitas consultas para um mesmo curso porque a cada consulta
        # seria calculada a média.
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if not media:
            return 0
        return round(media * 2) / 2 #média justa pela estátistica

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',  # nested relationship
            'media_avaliacoes'
        )

