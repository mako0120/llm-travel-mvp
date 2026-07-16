# AI Development Company Rules

## Source of work

- Every code or documentation change starts from an open GitHub Issue.
- Claude Code implements only Issues labeled `claude`.
- Claude branches use `claude/feature-<issue-number>-<slug>`.
- Codex branches use `codex/issue-<issue-number>-<slug>`.
- Pull requests must include `Closes #<issue-number>`.

## Review handoff

- `ai:claude-ready` means the Issue is ready for Claude Code or Cowork to receive.
- `ai:codex-waiting` means a Claude PR exists but is still a Draft.
- `ai:codex-review` means the PR is ready for Codex review.
- Codex verifies Issue scope, changed files, tests, CI, Vercel Preview, secrets, and approval boundaries.
- Review findings are recorded on the PR. Notion is updated after the result is known.

## Safety boundaries

- Never push directly to `main`.
- Never commit `.env.local`, credentials, tokens, or API keys.
- Do not change Production deployment, billing, authentication, databases, environment variables, or external-service settings without explicit approval.
- Do not make destructive database changes.
- Do not edit the same files concurrently with another implementation agent.

## Verification

Run the checks relevant to the change and report exact results in the PR:

```text
npm ci
npm run lint
npm run typecheck
npm run build
```

Documentation-only changes still require `git diff --check` and GitHub workflow validation.
