# MarkdownToConfluence
Bachelor 2022 - Anders Larsen &amp; Theis Tengs

This action converts your markdown files into the specified Atlassian Confluence space.

## Environment Variables
The necessary environment variables are as follows: 

`CONFLUENCE_URL`

The URL for the Atlassian network

`CONFLUENCE_SPACE_KEY`

The ID of the space that is being uploaded to.

`AUTH_TOKEN`

This is a base64 encoded string consisting of your Atlassian username together with an API token from Atlassian aswell.

An example could be:

username:api_token

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
          CONFLUENCE_URL: 'https://space.atlassian.net/wiki'
          CONFLUENCE_SPACE_ID: '~955037829'
          AUTH_TOKEN: ${{ secrets.AUTH_TOKEN }}
        uses: ./ # Uses an action in the root directory
        id: Convert
        with:
          fileslocation: './documentation'
```
