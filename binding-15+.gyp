{
  "targets": [{
    "target_name": "pc-util",
    "sources": [ ],
    "conditions": [
      ['OS=="mac"', {
        "sources": [
          "pcutil.mm"
        ],
        "xcode_settings": {
          "MACOSX_DEPLOYMENT_TARGET": "10.10",
          "OTHER_CPLUSPLUSFLAGS": ["-std=c++14", "-stdlib=libc++"],
          "OTHER_LDFLAGS": ["-framework CoreBluetooth -framework CoreFoundation -framework CoreLocation -framework AppKit -framework Contacts -framework Photos -framework EventKit -framework AVFoundation -framework Speech"]
        },
      }],
      ['OS=="win"', {
        "sources": [
          "pcutil.cpp"
        ],
        'defines': [
          'WIN32',
          'WIN32_LEAN_AND_MEAN'
        ],
        'link_settings': {
          'libraries': [
            '-lversion.lib'
          ]
        },
        'msvs_settings': {
          'VCCLCompilerTool': {
            # 'WarningLevel': '3',
            # 'DisableSpecificWarnings': ['4819'],
            # 'WarnAsError': 'false',
            # 'ExceptionHandling': '0',
            'AdditionalOptions': [
              # '/EHsc',
              '/utf-8'
            ]            
          }
        },
        'defines!': [
          '_USING_V110_SDK71_',
          '_HAS_EXCEPTIONS=0'
        ],
        'configurations': {
          'Release': {
            'msvs_settings': {
              'VCCLCompilerTool': {
                # 多线程 DLL (/MD)
                'RuntimeLibrary': '2',
                # 完全优化 /Os
                'Optimization': '2',
                # 使用内部函数 /Oi
                'EnableIntrinsicFunctions': 'true',
                # 程序数据库 (/Zi)
                'DebugInformationFormat': '3',
                'AdditionalOptions': [
                ]            
              }
            },
          },
          'Debug': {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeLibrary': '3',
                # 'WarningLevel': '3',
                # 'DisableSpecificWarnings': ['4819'],
                # 'WarnAsError': 'false',
                # 'ExceptionHandling': '0',
                'AdditionalOptions': [
                ]            
              }
            },
          }
        }
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