# -*- coding: utf-8 -*-

from django.template.defaultfilters import slugify


TIPO_TRANSACAO = (
    (1, 'Aluguel'),
    (2, 'Venda'),
)

TIPO_IMOVEL = (
    (1, 'Casa'),
    (2, 'Apartamento'),
    (3, 'Terreno'),
    (4, 'Chácara'),
)

FINALIDADE = (
    (1, 'Residencial'),
    (2, 'Comercial'),
    (3, 'Industrial'),
)


STATUS_CHOICES = (
    (1, u'Pré-Lançamento'),
    (2, u'Lançamento'),
    (3, u'Em Construção'),
    (4, u'Finalizado'),
)

STATUS_UNIDADES = (
    (1, 'Livre'),
    (2, 'Reservado'),
    (3, 'Vendido'),
)

STATUS_IMOVEIS = (
    (1, 'Livre'),
    (2, 'Alugado'),
    (3, 'Vendido'),
)

ESTADO_CIVIL = (
    (1, u'Solteiro(a)'),
    (2, u'Casado(a)'),
    (3, u'Viuvo(a)'),
    (4, u'Divorciado(a)'),
)

PROFISSOES = (
    (1, u'Advogado(a)'),
    (2, u'Agente de inseminação artificial'),
    (3, u'Agente Oficial da Propriedade Industrial'),
    (4, u'Ajudante de Cozinheiro(a)(Profissão Marítima)'),
    (5, u'Ajudante de Maquinista'),
    (6, u'Arquiteto(a)'),
    (7, u'Arrais de pesca local '),
    (8, u'Arrais de pesca '),
    (9, u'Biólogo(a)'),
    (10, u'Contramestre '),
    (11, u'Contramestre pescador '),
    (12, u'Cozinheiro (a) (Profissão Marítima)'),
    (13, u'Despachante Oficial '),
    (14, u'Dietista '),
    (15, u'Director(a) de escola de condução'),
    (16, u'Director(a) técnico da actividade transitária'),
    (17, u'Docente do Ensino Superior Politécnico'),
    (18, u'Docente do Ensino Superior Universitário'),
    (19, u'Educador(a) de Infância'),
    (20, u'Electricista(Profissão Marítima)'),
    (21, u'Empregado(a) de câmaras (Profissão Marítima)'),
    (22, u'Enfermeiro(a) Especialista em Enfermagem de Saúde Materna e Obstétrica'),
    (23, u'Enfermeiro(a) Responsável por Cuidados Gerais'),
    (24, u'Engenheiro(a) Agrónomo(a)'),
    (25, u'Engenheiro(a) Civil'),
    (26, u'Engenheiro(a) de Materiais'),
    (27, u'Engenheiro(a) do Ambiente'),
    (28, u'Engenheiro(a) Electrotécnico(a)'),
    (29, u'Engenheiro(a) Florestal'),
    (30, u'Engenheiro(a) Geógrafo(a)'),
    (31, u'Engenheiro(a) Geológo(a) e de Minas'),
    (32, u'Engenheiro(a) Informático(a)'),
    (33, u'Engenheiro(a) Mecânico(a)'),
    (34, u'Engenheiro(a) Metalúrgico(a) e de Materiais'),
    (35, u'Engenheiro(a) Naval'),
    (36, u'Engenheiro(a) Químico(a) e Biológico(a)'),
    (37, u'Engenheiro(a) Técnico(a) de Aeronáutica'),
    (38, u'Engenheiro(a) Técnico(a) de Agrária'),
    (39, u'Engenheiro(a) Técnico(a) de Alimentar'),
    (40, u'Engenheiro(a) Técnico(a) de Ambiente'),
    (41, u'Engenheiro(a) Técnico(a) de Civil'),
    (42, u'Engenheiro(a) Técnico(a) de Electrónica e Telecomunicações'),
    (43, u'Engenheiro(a) Técnico(a) de Energia e Sistemas de Potência'),
    (44, u'Engenheiro(a) Técnico(a) de Geográfica/Topográfica'),
    (45, u'Engenheiro(a) Técnico(a) de Geotecnia e Minas'),
    (46, u'Engenheiro(a) Técnico(a) de Industrial e da Qualidade'),
    (47, u'Engenheiro(a) Técnico(a) de Informática'),
    (48, u'Engenheiro(a) Técnico(a) de Mecânica'),
    (49, u'Engenheiro(a) Técnico(a) de Proteção Civil'),
    (50, u'Engenheiro(a) Técnico(a) de Química'),
    (51, u'Engenheiro(a) Técnico(a) de Segurança'),
    (52, u'Engenheiro(a) Técnico(a) de Transportes'),
    (53, u'Enólogo(a)'),
    (54, u'Examinador(a) de condução'),
    (55, u'Farmacêutico(a)'),
    (56, u'Fisioterapeuta '),
    (57, u'Higienista oral '),
    (58, u'Instalador(a) de infra-estruturas de telecomunicações em edifícios'),
    (59, u'Instalador(a) de redes de gás'),
    (60, u'Instrutor(a) de condução'),
    (61, u'Maquinista prático de 1ª, 2ª e 3ª classes '),
    (62, u'Marinheiro(a) de embarcação salva-vidas - pessoal de convés'),
    (63, u'Marinheiro(a) de Tráfego Local'),
    (64, u'Marinheiro(a) de 1ª e 2ª classes'),
    (65, u'Marinheiro(a) maquinista'),
    (66, u'Marinheiro(a) pescador'),
    (67, u'Mecânico(a) de Bordo'),
    (68, u'Mecânico(a) de aparelhos de gás'),
    (69, u'Mecânico(a) de auto/gás'),
    (70, u'Médico(a) (com formação médica de base)'),
    (71, u'Médico(a) Dentista'),
    (72, u'Médico(a) Especialista'),
    (73, u'Médico(a) Veterinário(a)'),
    (74, u'Mergulhador(a) Profissional'),
    (75, u'Mestre costeiro '),
    (76, u'Mestre costeiro pescador '),
    (77, u'Mestre de tráfego local '),
    (78, u'Mestre do largo pescador '),
    (79, u'Motorista de embarcação salva-vidas '),
    (80, u'Motorista de Taxi '),
    (81, u'Nutricionista '),
    (82, u'Oficial de pilotagem da marinha mercante '),
    (83, u'Oficial maquinista da marinha mercante '),
    (84, u'Oficial Radiotécnico(a) da marinha mercante '),
    (85, u'Operador de gruas flutuantes '),
    (86, u'Ortoprotésico(a)'),
    (87, u'Ortoptista '),
    (88, u'Pescador(a)'),
    (89, u'Professor(a) do Ensino Básico'),
    (90, u'Professor(a) do Ensino Secundário'),
    (91, u'Profissional de Banca nos Casinos'),
    (92, u'Projectista de Infra-estruturas de telecomunicações em edifícios'),
    (93, u'Projectista (de redes de gás) '),
    (94, u'Psicólogo(a)'),
    (95, u'Radiotelegrafista prático da classe A '),
    (96, u'Radiotelegrafista prático da classe B '),
    (97, u'Revisor(a) Oficial de Contas'),
    (98, u'Sapador(a) Florestal'),
    (99, u'Soldador(a)'),
    (100, u'Solicitador(a)'),
    (101, u'Técnico(a)'),
    (102, u'Técnico(a) de anatomia patológica, citológica e tanatológica'),
    (103, u'Técnico(a) de análises clínicas e de saúde pública'),
    (104, u'Técnico(a) de audiologia'),
    (105, u'Técnico(a) de cardiopneumologia'),
    (106, u'Técnico(a) de farmácia'),
    (107, u'Técnico(a) de gás'),
    (108, u'Técnico(a) de gás (auto)'),
    (109, u'Técnico(a) de medicina nuclear'),
    (110, u'Técnico(a) de neurofisiologia'),
    (111, u'Técnico(a) de prótese dentária'),
    (112, u'Técnico(a) de radiologia'),
    (113, u'Técnico(a) de radioterapia'),
    (114, u'Técnico(a) de saúde ambiental'),
    (115, u'Técnico(a) de segurança e higiene do trabalho'),
    (116, u'Técnico(a) Oficial de Contas'),
    (117, u'Técnico(a) responsável pela execução de instalações electricas de serviço particular'),
    (118, u'Técnico(a) responsável pela exploração de instalações eléctricas de serviço particular'),
    (119, u'Técnico(a) responsável pelo projecto das instalações eléctricas de serviço particular'),
    (120, u'Técnico(a) Superior'),
    (121, u'Terapeuta da fala '),
    (122, u'Terapeuta ocupacional'),
)


def rename_file_and_upload_to(objeto, arquivo):
    """
    Essa função irá normalizar como um slug, o nome do arquivo que está sendo 
    gravado e, irá gravá-lo em 
    /media/uploads/APPNAME_CLASSNAME/nome_do_arquivo_normalizado.extensao
    """
    import os
    caminho = str('%s_%s' % (
        objeto._meta.app_label, objeto.__class__.__name__)
    ).lower()
    nome, ext = os.path.splitext(arquivo)
    url = slugify(nome)
    return os.path.join('', caminho, url + ext)

