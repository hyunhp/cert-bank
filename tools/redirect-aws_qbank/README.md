# Redirect for the old aws_qbank Pages address

`hyunhp.github.io/aws_qbank/` stopped working when the repo was renamed to `cert-bank` (GitHub redirects git
URLs of a renamed repo, but not its Pages site). These two files restore the old address as a redirect that keeps
the path, query and `#exam=` / `#mock=` hash.

The automation token cannot create repositories, so this is a one-time manual step:

1. Create a new public repo named `aws_qbank` under `hyunhp` (empty, no README).
2. Upload `index.html` and `404.html` from this folder to its root.
3. Settings → Pages → Deploy from branch → `main` / root.

Trade-off: once a repo named `aws_qbank` exists again, GitHub stops redirecting old *git* clone URLs
(`github.com/hyunhp/aws_qbank.git`) to `cert-bank`. Local clones must point at the new URL:
`git remote set-url origin https://github.com/hyunhp/cert-bank.git`.
