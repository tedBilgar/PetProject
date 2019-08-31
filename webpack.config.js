const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
  mode: 'development',
  devtool: 'source-map',
  entry: path.join(__dirname, 'frontend', 'src', 'js', 'main.js'),
  output: {
    filename: '[name].js',
    path: path.join(__dirname, 'frontend', 'out')
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
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      }
    ]
  },
  devServer: {
     contentBase: './frontend/out'
  },
  plugins: [
      new HtmlWebpackPlugin({template: './frontend/index.html'}),
    new VueLoaderPlugin()
  ],
  resolve: {
      modules: [
          path.join(__dirname, 'frontend', 'src', 'js'),
          path.join(__dirname, 'node_modules'),
      ],
  }
}