---
layout: page
title: Acerca
permalink: /about/
published: true
---

<div class="page" markdown="1">

{% capture page_subtitle %}
<img
    class="me"
    alt="{{ author.name }}"
    src="{{ site.author.photo | relative_url }}"
    srcset="{{ site.author.photo2x | relative_url }} 2x"
/>
{% endcapture %}

{% include page/title.html title=page.title subtitle=page_subtitle %}

Las Humanidades Digitales es un área de reciente creación en la que convergen la computación y las humanidades. Combina las metodologías tradicionales propias de las humanidades con técnicas computaciones como estadística, bases de datos y minería de datos entre otras.
En el marco del proyecto PAPIIT IA106620, estudiantes de la licenciatura en Tecnología para la Información en Ciencias de la ENES Morelia nos dedicamos a explorar una colección de hechicería contemporánea. Nuestro trabajo ha consistido en tres áreas de exploración, el análisis del corpus mediante procesamiento natural del lenguaje, el análisis de la composición química de los hechizos y la visualización de los datos.

</div>
