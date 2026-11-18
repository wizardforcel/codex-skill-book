# Habilidad de Síntesis Metafísica

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab)](scripts/)


La habilidad de Síntesis Metafísica es un paquete reutilizable para agentes de inteligencia artificial enfocado en BaZi, Meihua Yishu, Liuyao, análisis direccional de Feng Shui y lectura de Tarot. No es solo una instrucción de adivinación. Es un flujo de trabajo estructurado que ayuda a un asistente de IA a elegir el sistema correcto, revisar las entradas, dar un veredicto, mostrar la evidencia, estimar el tiempo, proponer acciones y definir señales de verificación. Puede usarse con Codex, Claude Code o cualquier otro agente que pueda leer una carpeta local con instrucciones, referencias y scripts.

Muchas respuestas de adivinación generadas por IA se vuelven demasiado vagas. Mezclan astrología china, I Ching, Feng Shui y Tarot como si fueran el mismo lenguaje. A veces toman una sola señal, una sola carta o una sola oposición y la convierten en una conclusión enorme. Esta habilidad evita ese error. BaZi se usa para estructura de vida, ciclos de diez años, carrera, riqueza, matrimonio y salud. Meihua Yishu se usa para eventos cercanos, horarios, números, presagios y movimiento inmediato. Liuyao se usa para resultados concretos: contrato, puesto, jefe, salario, proyecto o relación específica. Feng Shui se usa para espacio, dirección, respaldo, puertas, ventanas, flujo, visibilidad y presión ambiental. Tarot se usa para dinámica psicológica, relaciones, decisiones y puntos de giro simbólicos.

La habilidad busca respuestas claras, pero no falsas certezas. Cada método se marca como `runnable`, `partial` o `blocked`. Si la hora de nacimiento no es segura, no se fuerza una lectura detallada del pilar de la hora. Si las seis líneas de Liuyao no tienen orden claro, la lectura Najia se limita. Si no hay plano ni brújula, el Feng Shui no se presenta como lectura profesional completa. Si el usuario ya dio cartas de Tarot, no se vuelven a sacar. Si el agente hace una tirada, el seed queda visible para que el resultado sea reproducible.

## Idiomas

- [inglés](README.md)
- [chino simplificado](README.zh-CN.md)
- [coreano](README.ko-KR.md)
- [japonés](README.ja-JP.md)
- [francés](README.fr-FR.md)
- [español](README.es-ES.md)

## Para quién es

Este repositorio es para usuarios que quieren dar a un agente de inteligencia artificial un método estable para responder preguntas metafísicas sin escribir una instrucción larga cada vez. También sirve como base para productos de consulta, asistentes personales, flujos internos de lectura simbólica o herramientas educativas sobre sistemas de adivinación. Los archivos de referencia mantienen cada método separado, los scripts evitan repetir operaciones deterministas y las plantillas de salida mantienen la respuesta clara.

La meta no es hacer la lectura más misteriosa. La meta es hacerla más legible. Una buena lectura debe decir cuál es la conclusión dominante, qué evidencia la sostiene, qué parte es débil, qué falta, qué puede verificarse y qué acción concreta se recomienda. El lenguaje puede ser simbólico, pero el proceso debe ser limpio.

## Sistemas compatibles

| Sistema | Resumen de unas 100 palabras | Archivo principal |
| --- | --- | --- |
| [BaZi / astrología china](https://es.wikipedia.org/wiki/Astrolog%C3%ADa_china) | BaZi, o Cuatro Pilares, usa año, mes, día y hora de nacimiento para construir una estructura simbólica basada en tallos celestiales, ramas terrestres y cinco fases. En esta habilidad se usa para tendencias de vida: carrera, riqueza, matrimonio, salud, ciclos decenales y activadores anuales. | `references/bazi.md` |
| [Meihua Yishu / I Ching](https://es.wikipedia.org/wiki/I_Ching) | Meihua Yishu es una lectura de imagen y número vinculada al Libro de los Cambios. Sirve para eventos próximos, horarios, números, direcciones, presagios y cambios repentinos. La habilidad distingue hexagrama principal, línea móvil, hexagrama mutuo, hexagrama transformado y relación Ti/Yong. | `references/meihua.md` |
| [Liuyao / Wenwanggua](https://en.wikipedia.org/wiki/Wenwanggua) | Liuyao lee seis líneas, líneas móviles, roles, relación con la otra parte y disparadores temporales para responder preguntas concretas. Es útil para contratos, ascensos, jefes, salarios, proyectos y relaciones específicas. La habilidad exige orden de abajo hacia arriba y limita la lectura si faltan datos Najia. | `references/liuyao.md` |
| [Feng Shui](https://es.wikipedia.org/wiki/Feng_shui) | Feng Shui estudia orientación, forma, flujo, respaldo, apertura, ruido, luz, privacidad y movimiento dentro de un espacio. Esta habilidad lee primero el entorno observable y luego la simbología direccional. Prioriza ajustes prácticos sobre remedios caros o afirmaciones imposibles de verificar. | `references/fengshui.md` |
| [Tarot](https://es.wikipedia.org/wiki/Tarot) | Tarot usa una tirada, posiciones, imágenes, palos, números, cartas derechas o invertidas y relaciones entre cartas para explorar psicología, vínculos y decisiones. Esta habilidad permite tiradas reproducibles con semilla, evitando repetir la tirada hasta obtener una respuesta agradable. | `references/tarot.md` |

## Método de respuesta

1. Reformular la pregunta real.
2. Elegir el sistema adecuado.
3. Revisar si las entradas son suficientes.
4. Marcar el método como `runnable`, `partial` o `blocked`.
5. Leer cada sistema por separado antes de sintetizar.
6. Sintetizar solo las señales compatibles.
7. Responder con veredicto, evidencia, tiempo, acción y señales de verificación.

Formato típico:

```text
Veredicto:
Evidencia:
Tiempo / fuerza:
Acción:
Señales de verificación:
Inferencias de baja confianza:
```

## Instalación para cualquier agente de inteligencia artificial

### Instalación universal

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis
cd ~/agent-skills/metaphysics-synthesis
python3 scripts/validate_skill.py
```

Luego indique al agente:

```text
Usa la habilidad local en ~/agent-skills/metaphysics-synthesis/SKILL.md. Carga solo el archivo de referencia adecuado para el sistema solicitado.
```

### Codex

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
python3 ~/.codex/skills/metaphysics-synthesis/scripts/validate_skill.py
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.claude/skills/metaphysics-synthesis
python3 ~/.claude/skills/metaphysics-synthesis/scripts/validate_skill.py
```

### Carpeta personalizada

```bash
AGENT_SKILLS_DIR="$HOME/.your-agent/skills"
mkdir -p "$AGENT_SKILLS_DIR"
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git "$AGENT_SKILLS_DIR/metaphysics-synthesis"
python3 "$AGENT_SKILLS_DIR/metaphysics-synthesis/scripts/validate_skill.py"
```

### Una copia compartida por varios agentes

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis

mkdir -p ~/.codex/skills ~/.claude/skills
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.codex/skills/metaphysics-synthesis
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.claude/skills/metaphysics-synthesis
```

## Ejemplos

```text
Analiza esta carta BaZi para carrera y riqueza entre 2026 y 2036. Separa estructura natal, suerte decenal, activadores anuales, conclusiones de alta confianza e inferencias de baja confianza.
```

```text
Usa Meihua Yishu para leer si este lanzamiento de producto puede crear un avance visible en mi carrera. La pregunta surgió el 2026-06-12 a las 10:36, y el presagio externo fue un gerente hablando de planificación al noroeste.
```

```text
Usa Liuyao para juzgar si este proyecto puede convertirse en la evidencia principal para una promoción. Las seis líneas de abajo hacia arriba son 5 / 4 / 25 / 12 / 22 / 17.
```

```text
Analiza mi puesto de trabajo con lógica de direcciones Feng Shui. Estoy mirando al sureste, mi gerente directo está al noroeste, el líder principal está al sur y otro gerente está al este.
```

```text
Haz una tirada de Tarot de cinco cartas para una decisión profesional. Muestra semilla, posiciones, cartas derechas o invertidas, veredicto, acción y señales de verificación.
```

## Scripts útiles

```bash
python3 scripts/meihua_calc.py time 2026 6 12 10
python3 scripts/meihua_calc.py num 22 5 18
python3 scripts/tarot_draw.py --spread relationship --question "¿Esta colaboración va a madurar?" --seed 42
python3 scripts/validate_skill.py
python3 scripts/privacy_check.py
```

## Límites de seguridad

Este repositorio trata la adivinación como un marco cultural, simbólico, reflexivo y estratégico. No sustituye consejos médicos, legales, financieros, psicológicos, de emergencia o de seguridad. En temas de alto riesgo, use primero evidencia directa y profesionales cualificados.

## Licencia

MIT License. Consulte [LICENSE](LICENSE).
