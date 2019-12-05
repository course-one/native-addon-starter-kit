{
  "targets": [
    {
      "target_name": "greet",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [
        "./src/greeting.cpp",
        "./src/index.cpp"
      ],
      "include_dirs": [
        "./node_modules/node-addon-api"
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}