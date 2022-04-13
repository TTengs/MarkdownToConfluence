# MarkdownToConfluence
Bachelor 2022 - Anders Larsen &amp; Theis Tengs

This action converts your markdown files into the specified Atlassian Confluence space.

## Environment Variables
Tekst
## Inputs

## `fileslocation`

**Required** The path to the folder containing the markdown documentation. Default `.\`.

## Outputs

## Ikke lige nogle indtil nu
## Example usage

- name: Conversion step
        env:
          CONFLUENCE_URL: 'https://at-bachelor.atlassian.net/wiki'
          CONFLUENCE_NAME: 'Anders Larsen'
          CONFLUENCE_SPACE_ID: '~955037829'
          AUTH_TOKEN: ${{ secrets.CONFLUENCE_URL }}
        uses: TTengs/MarkdownToConfluence@v0.5
        id: Convert
        with:
          fileslocation: './documentation'