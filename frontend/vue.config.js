const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      // Proxy API requests to Django backend
      '^/api/v1': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  }
})
