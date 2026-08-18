# Security

## Reporting

If you believe you have found a security or privacy problem in this Project — a leaked credential, an exposed client name, a file that should never have been committed — report it to **security@productside.com**. Do not open a public issue.

Please include what you found, where, and how you found it. You will get an acknowledgment.

## What This Project Is

This Project contains instructional materials: prose skills, references, and worked examples. It runs no service, stores no user data, and exposes no endpoint. The Python utilities under `scripts/` validate and package documents; they accept no untrusted input beyond the Project's own files.

The realistic risks here are therefore about **content**, not code:

- a credential or token committed by accident
- a client or customer name reaching a public Project
- a file type that belongs in SharePoint rather than in a Project
- an example that reads as a factual claim about a real company

The Content Guard workflow in `.github/workflows/content-guard.yml` blocks the first three on every push and pull request. The fourth is handled by the standard in `docs/SKILL-SPEC.md`: every example is synthetic and labeled as such.

## Blocked Terms

The blocked-terms list used by the Content Guard is held in a repository or organization secret, never in a file in the tree. **A list of client names committed to a public Project is itself a client list.**

## Scope of the Methods Taught

The collection methods in this Project are limited to public, published, filed, or observable material. If you find guidance here that could be read as endorsing pretexting, solicitation of confidential information, or access to anything behind an authentication boundary, that is a defect — report it as one.
