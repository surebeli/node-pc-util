{
  "targets": [{
    "target_name": "pcutil",
    "sources": [ ],
    "conditions": [
      ['OS=="mac"', {
        "sources": [
          "pcutil.mm"
        ],
        "xcode_settings": {
          "MACOSX_DEPLOYMENT_TARGET": "10.10",
          "OTHER_CPLUSPLUSFLAGS": ["-std=c++14", "-stdlib=libc++"],
          "OTHER_LDFLAGS": ["-framework CoreBluetooth -framework CoreFoundation -framework CoreLocation -framework AppKit -framework Speech -framework Contacts -framework Photos -framework EventKit -framework AVFoundation"]
        },
      }]
    ],
    'include_dirs': [
      "<!@(node -p \"require('node-addon-api').include\")"
    ],
    'libraries': [],
    'dependencies': [
      "<!(node -p \"require('node-addon-api').gyp\")"
    ],
    'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
  }]
}