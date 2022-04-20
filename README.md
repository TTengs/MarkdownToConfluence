# MarkdownToConfluence
Bachelor 2022 - Anders Larsen &amp; Theis Tengs

This action converts your markdown files into the specified Atlassian Confluence space.

## Environment Variables
The necessary environment variables are as follows: 

`CONFLUENCE_URL`

The URL for the, Atlassian network

`CONFLUENCE_SPACE_KEY`

The key of the space that is being uploaded to.

`AUTH_TOKEN`

This is a base64 encoded string consisting of your Atlassian username (email) together with an API token from Atlassian aswell.

An example could be:

your@email.com:api_token

This then needs to be base64 encoded and added as a github secret with the name of `AUTH_TOKEN`.
## Inputs

### `fileslocation`

**Required** The path to the folder containing the markdown documentation. Default `.\`.

## Outputs

### Ikke lige nogle indtil nu
## Example usage

```yaml
- name: Conversion step
        env:
          CONFLUENCE_URL: 'https://network.atlassian.net/wiki'
          CONFLUENCE_SPACE_KEY: 'spaceKey'
          AUTH_TOKEN: ${{ secrets.AUTH_TOKEN }}
        uses: TTengs/MarkdownToConfluence@v1.1
        id: Convert
        with:
          fileslocation: './documentation'
```
