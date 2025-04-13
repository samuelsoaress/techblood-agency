import re

def flaskify_static_paths(html: str) -> str:
    # Lista de atributos que queremos substituir
    attrs = ['src', 'href', 'data-src', 'data-srcset', 'srcset', 'url']

    for attr in attrs:
        # Regex para encontrar atributos com caminhos relativos
        pattern = re.compile(rf'({attr})=["\'](?!https?:|{{|data:|#)(\.?/?(?:js|css|images|fonts|wp-content|plugins)/[^"\']+)["\']')
        html = pattern.sub(rf'\1="{{{{ url_for(\'static\', filename=\'\2\') }}}}"', html)

    # Substituir fontes dentro do @font-face (CSS)
    font_pattern = re.compile(r"""url\(['"](\.\./fonts/[^'"]+)['"]\)""")
    html = font_pattern.sub(r"url('{{ url_for('static', filename='\1') }}')", html)

    return html

import re

def flaskify_src_and_srcset(html: str) -> str:
    # Substitui src="algum/caminho.ext" por src="{{ url_for('static', filename='algum/caminho.ext') }}"
    html = re.sub(
        r'src="(?!https?:|data:|{{)([^"]+)"',
        r'src="{{ url_for(\'static\', filename=\'\1\') }}"',
        html
    )

    # Substitui cada caminho dentro de srcset (ex: imagens com resoluções diferentes)
    def replace_srcset(match):
        srcset_value = match.group(1)
        parts = srcset_value.split(',')
        replaced = []
        for part in parts:
            file_path = part.strip().split(' ')[0]
            descriptor = part.strip()[len(file_path):]
            if file_path.startswith(('http', 'data:', '{{')):
                replaced.append(file_path + descriptor)
            else:
                replaced.append(f"{{{{ url_for('static', filename='{file_path}') }}}}{descriptor}")
        return f'srcset="{" , ".join(replaced)}"'

    html = re.sub(r'srcset="([^"]+)"', replace_srcset, html)

    return html

# Exemplo de uso:
with open('social_media.html', 'r', encoding='utf-8') as f:
    original_html = f.read()

flask_ready_html = flaskify_static_paths(original_html)
flask_ready_html = flaskify_src_and_srcset(flask_ready_html)

with open('social_media2.html', 'w', encoding='utf-8') as f:
    f.write(flask_ready_html)

print("Substituições feitas! Arquivo salvo como 'seuarquivo_flask.html'")
