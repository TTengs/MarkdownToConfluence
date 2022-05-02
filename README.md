# MarkdownToConfluence
Bachelor 2022 - Anders Larsen &amp; Theis Tengs

This action converts your markdown files into the specified Atlassian Confluence space.

# Setup
## API User Token
First you need to create an API token for the user, you want to use for the action. We recommend that you create a new user, that is only used for this action, in order to get the full benefits from the action. See (here)[https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/] for how to set up your API token.

## Environment Variables
The necessary environment variables are as follows: 

`CONFLUENCE_URL`

The base URL for the Atlassian network. Follows the form: 'https://<your-network-name>.atlassian.net'

`CONFLUENCE_SPACE_KEY`

The key of the space that is being uploaded to. Can be found in the URL for your space. More info (here)[https://confluence.atlassian.com/doc/space-keys-829076188.html]

`AUTH_USERNAME`
The email used for the user connected to the API token. We recommend setting this as a GitHub secret.
        
`AUTH_API_TOKEN`
The API token generated for the user. We recommend setting this as a GitHub secret.

## Inputs

### `fileslocation`

**Required** The path to the folder containing the markdown documentation. Default `.\`.

## Outputs

### Ikke lige nogle indtil nu

## Example usage

Without github secrets:
```yaml
- name: Conversion step
        env:
          CONFLUENCE_URL: 'https://network.atlassian.net/wiki'
          CONFLUENCE_SPACE_KEY: 'spaceKey'
          AUTH_USERNAME: 'your@email.com'
          AUTH_API_TOKEN: 'PeRsOnalApItOKen'
        uses: TTengs/MarkdownToConfluence@latest
        with:
          fileslocation: './documentation'
```
        
With GitHub actions
```yaml
- name: Conversion step
        env:
          CONFLUENCE_URL: 'https://network.atlassian.net/wiki'
          CONFLUENCE_SPACE_KEY: 'spaceKey'
          AUTH_USERNAME: ${{ secrets.AUTH_USERNAME }}
          AUTH_API_TOKEN: ${{ secrets.AUTH_API_TOKEN }}
        uses: TTengs/MarkdownToConfluence@latest
        with:
          fileslocation: './documentation'
```
