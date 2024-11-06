from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from .models import UserProfile, VideoProgress  # Importa UserProfile e VideoProgress

# View de Login personalizada para autenticação
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        empresa_input = request.POST.get('empresa')  # Empresa inserida no formulário

        # Autentica o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Verifica se o usuário possui um perfil e se a empresa coincide
            if UserProfile.objects.filter(user=user, empresa=empresa_input).exists():
                login(request, user)
                return redirect('index')  # Redireciona para a página index após login bem-sucedido
            else:
                messages.error(request, "A empresa fornecida não corresponde ao perfil.")
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")

        return render(request, 'login.html')


# Views baseadas em classe para renderizar templates
class IndexView(TemplateView):
    template_name = 'index.html'


    perguntas_respostas = {
        1: "O que é uma isca 410? : Uma Isca 410 é um dispositivo rastreador de carga, usado para monitoramento e proteção de mercadorias em trânsito. Ele é posicionado de forma discreta em caminhões ou containers, permitindo que empresas acompanhem a localização em tempo real e detectem movimentações suspeitas, ajudando na recuperação de cargas roubadas.",
        2: "O que é uma isca gs419 lora? :Uma Isca GS419 LoRa é um rastreador de carga equipado com tecnologia LoRa (Long Range), que permite comunicação de longa distância com baixo consumo de energia. Ela é usada para monitoramento de mercadorias em áreas remotas ou onde o sinal de celular é limitado, garantindo rastreamento contínuo em tempo real e segurança da carga.",
        3: "O que é uma isca gl33? : Uma Isca GL33 é um dispositivo rastreador compacto para cargas, projetado para monitoramento discreto e recuperação de mercadorias em caso de roubo. Ele utiliza tecnologias de geolocalização, como GPS e conectividade celular, para fornecer a localização em tempo real, permitindo que empresas acompanhem e protejam suas cargas durante o transporte.",
        4: "O que é uma isca 4410? : Uma Isca 4410 é um dispositivo de rastreamento especializado em monitoramento de cargas, geralmente utilizado para segurança e recuperação de mercadorias em trânsito. Esse tipo de isca é discreto, com alta duração de bateria, e pode ser colocado de forma oculta em caminhões ou containers. A Isca 4410 utiliza tecnologia GPS e conectividade celular para fornecer atualizações em tempo real sobre a localização da carga, auxiliando no combate ao roubo de mercadorias e aumentando a segurança logística.",
        5: "Como e onde inserir a isca? :A isca deve ser inserida de forma discreta em locais ocultos da carga, como compartimentos internos, debaixo de estofados ou entre produtos empilhados, garantindo boa conectividade para o sinal GPS e em áreas de difícil acesso para evitar detecção, além de variar o local de posicionamento a cada viagem para aumentar a segurança.",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perguntas_formatadas = {}
        for key, value in self.perguntas_respostas.items():
            pergunta, resposta = value.split(':', 1)
            perguntas_formatadas[key] = {
                'pergunta': pergunta.strip(),
                'resposta': resposta.strip()
            }
        context['perguntas_respostas'] = perguntas_formatadas
        print("Conteúdo de perguntas_respostas:", context['perguntas_respostas'])  # Debug para verificar o conteúdo
        return context

class EquipamentoView(TemplateView):
    template_name = "equipamento.html"

class PlataformaView(TemplateView):
    template_name = "plataforma.html"

class InsercaoView(TemplateView):
    template_name = "insercao.html"

class PilaresView(TemplateView):
    template_name = 'pilares.html'

def mark_pilar_watched(request):
    if request.method == 'POST' and request.user.is_authenticated:
        progress, created = VideoProgress.objects.get_or_create(user=request.user)
        progress.pilar_watched = True
        progress.save()
        return redirect('equipamento-selecao')  # Redireciona para o próximo card
    return redirect('pilares')


# Views para os vídeos
class VideoIsca2GView(TemplateView):
    template_name = "video-isca2g.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, *args, **kwargs)
        return redirect('login')


class VideoIsca4GView(TemplateView):
    template_name = "video-isca4g.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, *args, **kwargs)
        return redirect('login')


class VideoQueclinkView(TemplateView):
    template_name = "video-queclink.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, *args, **kwargs)
        return redirect('login')


class VideoPilaresView(TemplateView):
    template_name = 'video-pilares.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, *args, **kwargs)
        return redirect('login')
    
class VideoIsca419View(TemplateView):
    template_name = 'video-isca419.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, *args, **kwargs)
        return redirect('login')

class VideoInsercaoView(TemplateView):
    template_name = 'video-insercao.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, *args, **kwargs)
        return redirect('login')
    
class VideoPlataformaView(TemplateView):
    template_name = 'video-plataforma.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, *args, **kwargs)
        return redirect('login')
    
class EquipamentoSelecaoView(TemplateView):
    template_name = 'equipamento-selecao.html'

from django.views.generic import TemplateView
from django.shortcuts import render

class ChatbotView(TemplateView):
    template_name = "index.html"


    perguntas_respostas = {
        1: "O que é uma isca 410? : Uma Isca 410 é um dispositivo rastreador de carga, usado para monitoramento e proteção de mercadorias em trânsito. Ele é posicionado de forma discreta em caminhões ou containers, permitindo que empresas acompanhem a localização em tempo real e detectem movimentações suspeitas, ajudando na recuperação de cargas roubadas.",
        2: "O que é uma isca gs419 lora? :Uma Isca GS419 LoRa é um rastreador de carga equipado com tecnologia LoRa (Long Range), que permite comunicação de longa distância com baixo consumo de energia. Ela é usada para monitoramento de mercadorias em áreas remotas ou onde o sinal de celular é limitado, garantindo rastreamento contínuo em tempo real e segurança da carga.",
        3: "O que é uma isca gl33? : Uma Isca GL33 é um dispositivo rastreador compacto para cargas, projetado para monitoramento discreto e recuperação de mercadorias em caso de roubo. Ele utiliza tecnologias de geolocalização, como GPS e conectividade celular, para fornecer a localização em tempo real, permitindo que empresas acompanhem e protejam suas cargas durante o transporte.",
        4: "O que é uma isca 4410? : Uma Isca 4410 é um dispositivo de rastreamento especializado em monitoramento de cargas, geralmente utilizado para segurança e recuperação de mercadorias em trânsito. Esse tipo de isca é discreto, com alta duração de bateria, e pode ser colocado de forma oculta em caminhões ou containers. A Isca 4410 utiliza tecnologia GPS e conectividade celular para fornecer atualizações em tempo real sobre a localização da carga, auxiliando no combate ao roubo de mercadorias e aumentando a segurança logística.",
        5: "Como e onde inserir a isca? :A isca deve ser inserida de forma discreta em locais ocultos da carga, como compartimentos internos, debaixo de estofados ou entre produtos empilhados, garantindo boa conectividade para o sinal GPS e em áreas de difícil acesso para evitar detecção, além de variar o local de posicionamento a cada viagem para aumentar a segurança.",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perguntas_formatadas = {}
        for key, value in self.perguntas_respostas.items():
            pergunta, resposta = value.split(':', 1)
            perguntas_formatadas[key] = {
                'pergunta': pergunta.strip(),
                'resposta': resposta.strip()
            }
        context['perguntas_respostas'] = perguntas_formatadas
        print("Conteúdo de perguntas_respostas:", context['perguntas_respostas'])  # Debug para verificar o conteúdo
        return context