"""Internal API endpoint constant library.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

_sample_uploads_endpoints = [
  [
    "GetSampleV3",
    "GET",
    "/samples/entities/samples/v3",
    "Retrieves the file associated with the given ID (SHA256)",
    "sample_uploads",
    [
      {
        "type": "string",
        "description": "User UUID",
        "name": "X-CS-USERUUID",
        "in": "header"
      },
      {
        "type": "string",
        "description": "The file SHA256.",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "default": False,
        "description": "Flag whether the sample should be zipped and password protected with pass='infected'",
        "name": "password_protected",
        "in": "query"
      }
    ]
  ],
  [
    "UploadSampleV3",
    "POST",
    "/samples/entities/samples/v3",
    "Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint.",
    "sample_uploads",
    [
      {
        "type": "string",
        "description": "User UUID",
        "name": "X-CS-USERUUID",
        "in": "header"
      },
      {
        "description": "Content of the uploaded sample in binary format. For example, use `--data-binary "
        "@$FILE_PATH` when using cURL. Max file size: 100 MB.\n\nAccepted file formats:\n\n- Portable "
        "executables: `.exe`, `.scr`, `.pif`, `.dll`, `.com`, `.cpl`, etc.\n- Office documents: `.doc`, "
        "`.docx`, `.ppt`, `.pps`, `.pptx`, `.ppsx`, `.xls`, `.xlsx`, `.rtf`, `.pub`\n- PDF\n- APK\n- "
        "Executable JAR\n- Windows script component: `.sct`\n- Windows shortcut: `.lnk`\n- Windows help: "
        "`.chm`\n- HTML application: `.hta`\n- Windows script file: `.wsf`\n- Javascript: `.js`\n- Visual "
        "Basic: `.vbs`,  `.vbe`\n- Shockwave Flash: `.swf`\n- Perl: `.pl`\n- Powershell: `.ps1`, `.psd1`, "
        "`.psm1`\n- Scalable vector graphics: `.svg`\n- Python: `.py`\n- Linux ELF executables\n- Email "
        "files: MIME RFC 822 `.eml`, Outlook `.msg`.",
        "name": "body",
        "in": "body",
        "required": True
      },
      {
        "type": "file",
        "description": "The binary file.",
        "name": "upfile",
        "in": "formData",
        "required": True
      },
      {
        "type": "string",
        "description": "Name of the file.",
        "name": "file_name",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "A descriptive comment to identify the file for other users.",
        "name": "comment",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": True,
        "description": "Defines visibility of this file in Falcon MalQuery, either via the API or the "
        "Falcon console.\n\n- `true`: File is only shown to users within your customer account\n- `false`: "
        "File can be seen by other CrowdStrike customers \n\nDefault: `true`.",
        "name": "is_confidential",
        "in": "query"
      }
    ]
  ],
  [
    "DeleteSampleV3",
    "DELETE",
    "/samples/entities/samples/v3",
    "Removes a sample, including file, meta and submissions from the collection",
    "sample_uploads",
    [
      {
        "type": "string",
        "description": "User UUID",
        "name": "X-CS-USERUUID",
        "in": "header"
      },
      {
        "type": "string",
        "description": "The file SHA256.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ]
]
