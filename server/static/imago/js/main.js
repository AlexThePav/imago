$('.navbar-nav div a').filter(function(){;
  return location.href.indexOf(this.href) != -1;
}).addClass('active');