<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banners/dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/banners/light.svg">
  <img alt="Zaid Bharde GitHub profile banner" src="./assets/banners/dark.svg" width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/zaid-bharde-472933334/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>&nbsp;&nbsp;
  <a href="https://www.instagram.com/zxidd09/"><img src="https://img.shields.io/badge/Instagram-090608?style=for-the-badge&logo=instagram&logoColor=f3b84d" alt="Instagram"></a>&nbsp;&nbsp;
  <a href="mailto:zaidbharde09@gmail.com"><img src="https://img.shields.io/badge/Gmail-090608?style=for-the-badge&logo=gmail&logoColor=f3b84d" alt="Email"></a>
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=zaidbharde&theme=dark&hide_border=true&background=090608&ring=f3b84d&fire=f3b84d&currStreakLabel=fff1dd&sideLabels=b9a790&dates=b9a790" alt="GitHub streak" width="100%">
</p>

<p align="center">
  <img src="https://YOUR-GITHUB-README-STATS-VERCEL-APP.vercel.app/api?username=zaidbharde&show_icons=true&hide_rank=true&hide_border=true&bg_color=090608&title_color=f3b84d&text_color=fff1dd&icon_color=f3b84d" alt="GitHub stats" width="49%">
  <img src="https://YOUR-GITHUB-README-STATS-VERCEL-APP.vercel.app/api/top-langs/?username=zaidbharde&layout=compact&hide_border=true&bg_color=090608&title_color=f3b84d&text_color=fff1dd" alt="Top languages" width="49%">
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/zaidbharde/zaidbharde/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/zaidbharde/zaidbharde/output/github-contribution-grid-snake.svg">
  <img alt="GitHub contribution snake" src="https://raw.githubusercontent.com/zaidbharde/zaidbharde/output/github-contribution-grid-snake-dark.svg" width="100%">
</picture>

## Manual setup checklist

1. Create the profile repo named `zaidbharde` under the `zaidbharde` GitHub account and upload this README plus `assets/banners/dark.svg`, `assets/banners/light.svg`, and `.github/workflows/snake.yml`.
2. In this repo, go to Settings > Actions > General > Workflow permissions and select "Read and write permissions". This is the repo setting, not the account setting.
3. Run the "Generate contribution snake" workflow once. Add the snake `<picture>` only after the Action runs green, because the `output` branch does not exist before that.
4. Fork `anuraghazra/github-readme-stats`, create a classic GitHub token from Settings > Developer settings > Personal access tokens > Tokens (classic), choose `repo` scope, no expiration, copy it once, and never paste it publicly.
5. Import the fork on Vercel Hobby, add environment variable `PAT_1` with that token, deploy, then replace `YOUR-GITHUB-README-STATS-VERCEL-APP` above with your Vercel app name.

Note: `hide_rank=true` is intentional. The rank is heavily affected by stars and can be misleading for newer profiles, while the other cards show more useful activity and language signals.
