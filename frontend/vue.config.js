module.exports = {
  publicPath: '/',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000/',
      },
      '/static/posters': {
        target: 'http://localhost:8000/',
      },
    }
  },
  css: {
    loaderOptions: {
      sass: {
        prependData: `@import "@/styles/_variables.scss";
                      @import "@/styles/_navs.scss";
                      @import "@/styles/_movies.scss";
                      @import "@/styles/_spacing.scss";
                      @import "@/styles/_btn.scss";
                      @import "@/styles/_transition.scss";
                      @import "@/styles/_admin.scss";
                      @import "@/styles/_profile.scss";
                      @import "@/styles/_sign.scss";
                      @import "@/styles/_subscription.scss";
                      @import "@/styles/_fa-icon.scss";
                      @import "@/styles/_ratingsNew.scss";
                      @import "@/styles/_shared-styles.scss";`
      }
    }
  }
};
