export BROWSER=google-chrome

jupyter nbconvert state_machines.ipynb --to slides  --reveal-prefix reveal.js.350 --post serve --SlidesExporter.reveal_theme=simple
