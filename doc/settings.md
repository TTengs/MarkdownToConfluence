# Space settings
The root folder for your documentation can contain a settings.json file. This file can specify settings for how your documentation should be parsed and uploaded to confluence.

---
## Settings

### `parent_page`
The name of the parent page for all of your documentation. This defaults to 'Overview', which is the standard root page for confluence spaces.

Type:     String  
Required: No

---
### `modules`
This is a list of all the modules you want to be used in your system. Only modules listed here, will be used. If this option is not specified, all modules will be used.

Available modules:
 - mermaid
 - jira-tickets
 - attachment_link
 - table_of_contents

Type:     List of Strings  
Required: No