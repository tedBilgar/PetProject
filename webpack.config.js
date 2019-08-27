const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'development',
  devtool: 'source-map',
  entry: {
    main: './frontend/src/js/main.js'
  },
  output: {
    filename: '[name].js',
    path: path.join(__dirname, './frontend/out')
  },
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      }
    ]
  },
  devServer: {
     contentBase: './frontend/out'
  },
  plugins: [
    new HtmlWebpackPlugin({template: './frontend/index.html'})
  ]
}