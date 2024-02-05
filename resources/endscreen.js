(
    function (g) {
      var window = this;
      'use strict';
      var arb = function (a, b) {
        a.jb('onAutonavCoundownStarted', b)
      },
      l6 = function (a, b, c) {
        g.nv(a.element, 'ytp-suggestion-set', !!b.videoId);
        var d = b.playlistId;
        c = b.Xg(c ? c : 'mqdefault.jpg');
        var e = null,
        f = null;
        b instanceof g.fT &&
        (
          b.lengthText ? (e = b.lengthText || null, f = b.Wv || null) : b.lengthSeconds &&
          (e = g.yH(b.lengthSeconds), f = g.yH(b.lengthSeconds, !0))
        );
        var h = !!d;
        d = h &&
        'RD' === g.eRa(d).type;
        var l = b instanceof g.fT ? b.isLivePlayback : null,
        m = b instanceof g.fT ? b.isUpcoming : null,
        n = b.author,
        p = b.shortViewCount,
        q = b.publishedTimeText,
        r = [],
        t = [];
        n &&
        r.push(n);
        p &&
        (r.push(p), t.push(p));
        q &&
        t.push(q);
        c = {
          title: b.title,
          author: n,
          author_and_views: r.join(' • '),
          aria_label: b.ariaLabel ||
          g.FK('Watch $TITLE', {
            TITLE: b.title
          }),
          duration: e,
          timestamp: f,
          url: b.Nk(),
          is_live: l,
          is_upcoming: m,
          is_list: h,
          is_mix: d,
          background: c ? 'background-image: url(' + c + ')' : '',
          views_and_publish_time: t.join(' • '),
          autoplayAlternativeHeader: b.Wr
        };
        b instanceof g.eT &&
        (c.playlist_length = b.playlistLength);
        a.update(c)
      },
      m6 = function (a) {
        var b = a.U(),
        c = b.D;
        g.V.call(
          this,
          {
            I: 'a',
            S: 'ytp-autonav-suggestion-card',
            Y: {
              href: '{{url}}',
              target: c ? b.W : '',
              'aria-label': '{{aria_label}}',
              'data-is-live': '{{is_live}}',
              'data-is-list': '{{is_list}}',
              'data-is-mix': '{{is_mix}}',
              'data-is-upcoming': '{{is_upcoming}}'
            },
            V: [
              {
                I: 'div',
                Ma: [
                  'ytp-autonav-endscreen-upnext-thumbnail',
                  'ytp-autonav-thumbnail-small'
                ],
                Y: {
                  style: '{{background}}'
                },
                V: [
                  {
                    I: 'div',
                    Y: {
                      'aria-label': '{{timestamp}}'
                    },
                    Ma: [
                      'ytp-autonav-timestamp'
                    ],
                    ya: '{{duration}}'
                  },
                  {
                    I: 'div',
                    Ma: [
                      'ytp-autonav-live-stamp'
                    ],
                    ya: 'Live'
                  },
                  {
                    I: 'div',
                    Ma: [
                      'ytp-autonav-upcoming-stamp'
                    ],
                    ya: 'Upcoming'
                  },
                  {
                    I: 'div',
                    S: 'ytp-autonav-list-overlay',
                    V: [
                      {
                        I: 'div',
                        S: 'ytp-autonav-mix-text',
                        ya: 'Mix'
                      },
                      {
                        I: 'div',
                        S: 'ytp-autonav-mix-icon'
                      }
                    ]
                  }
                ]
              },
              {
                I: 'div',
                Ma: [
                  'ytp-autonav-endscreen-upnext-title',
                  'ytp-autonav-title-card'
                ],
                ya: '{{title}}'
              },
              {
                I: 'div',
                Ma: [
                  'ytp-autonav-endscreen-upnext-author',
                  'ytp-autonav-author-card'
                ],
                ya: '{{author}}'
              },
              {
                I: 'div',
                Ma: [
                  'ytp-autonav-endscreen-upnext-author',
                  'ytp-autonav-view-and-date-card'
                ],
                ya: '{{views_and_publish_time}}'
              }
            ]
          }
        );
        this.J = a;
        this.suggestion = null;
        this.j = c;
        this.Ra('click', this.onClick);
        this.Ra('keypress', this.onKeyPress)
      },
      n6 = function (a, b) {
        b = void 0 === b ? !1 : b;
        g.V.call(this, {
          I: 'div',
          S: 'ytp-autonav-endscreen-countdown-overlay'
        });
        var c = this;
        this.N = b;
        this.G = this.K = void 0;
        this.C = 0;
        this.container = new g.V({
          I: 'div',
          S: 'ytp-autonav-endscreen-countdown-container'
        });
        g.M(this, this.container);
        this.container.Ja(this.element);
        b = a.U();
        var d = b.D;
        this.J = a;
        this.suggestion = null;
        this.onVideoDataChange('newdata', this.J.getVideoData());
        this.T(a, 'videodatachange', this.onVideoDataChange);
        this.j = new g.V({
          I: 'div',
          S: 'ytp-autonav-endscreen-upnext-container',
          Y: {
            'aria-label': '{{aria_label}}',
            'data-is-live': '{{is_live}}',
            'data-is-list': '{{is_list}}',
            'data-is-mix': '{{is_mix}}',
            'data-is-upcoming': '{{is_upcoming}}'
          },
          V: [
            {
              I: 'div',
              S: 'ytp-autonav-endscreen-upnext-header'
            },
            {
              I: 'div',
              S: 'ytp-autonav-endscreen-upnext-alternative-header',
              ya: '{{autoplayAlternativeHeader}}'
            },
            {
              I: 'a',
              S: 'ytp-autonav-endscreen-link-container',
              Y: {
                href: '{{url}}',
                target: d ? b.W : ''
              },
              V: [
                {
                  I: 'div',
                  S: 'ytp-autonav-endscreen-upnext-thumbnail',
                  Y: {
                    style: '{{background}}'
                  },
                  V: [
                    {
                      I: 'div',
                      Y: {
                        'aria-label': '{{timestamp}}'
                      },
                      Ma: [
                        'ytp-autonav-timestamp'
                      ],
                      ya: '{{duration}}'
                    },
                    {
                      I: 'div',
                      Ma: [
                        'ytp-autonav-live-stamp'
                      ],
                      ya: 'Live'
                    },
                    {
                      I: 'div',
                      Ma: [
                        'ytp-autonav-upcoming-stamp'
                      ],
                      ya: 'Upcoming'
                    }
                  ]
                },
                {
                  I: 'div',
                  S: 'ytp-autonav-endscreen-video-info',
                  V: [
                    {
                      I: 'div',
                      S: 'ytp-autonav-endscreen-premium-badge'
                    },
                    {
                      I: 'div',
                      S: 'ytp-autonav-endscreen-upnext-title',
                      ya: '{{title}}'
                    },
                    {
                      I: 'div',
                      S: 'ytp-autonav-endscreen-upnext-author',
                      ya: '{{author}}'
                    },
                    {
                      I: 'div',
                      S: 'ytp-autonav-view-and-date',
                      ya: '{{views_and_publish_time}}'
                    },
                    {
                      I: 'div',
                      S: 'ytp-autonav-author-and-view',
                      ya: '{{author_and_views}}'
                    }
                  ]
                }
              ]
            }
          ]
        });
        g.M(this, this.j);
        this.j.Ja(this.container.element);
        d ||
        this.T(
          this.j.Ha('ytp-autonav-endscreen-link-container'),
          'click',
          this.IS
        );
        this.J.createClientVe(this.container.element, this, 115127);
        this.J.createClientVe(
          this.j.Ha('ytp-autonav-endscreen-link-container'),
          this,
          115128
        );
        this.overlay = new g.V({
          I: 'div',
          S: 'ytp-autonav-overlay'
        });
        g.M(this, this.overlay);
        this.overlay.Ja(this.container.element);
        this.B = new g.V({
          I: 'div',
          S: 'ytp-autonav-endscreen-button-container'
        });
        g.M(this, this.B);
        this.B.Ja(this.container.element);
        this.cancelButton = new g.V({
          I: 'button',
          Ma: [
            'ytp-autonav-endscreen-upnext-button',
            'ytp-autonav-endscreen-upnext-cancel-button',
            b.L('web_modern_buttons') ? 'ytp-autonav-endscreen-upnext-button-rounded' : ''
          ],
          Y: {
            'aria-label': 'Cancel auto-play'
          },
          ya: 'Cancel'
        });
        g.M(this, this.cancelButton);
        this.cancelButton.Ja(this.B.element);
        this.cancelButton.Ra('click', this.N1, this);
        this.J.createClientVe(this.cancelButton.element, this, 115129);
        this.playButton = new g.V({
          I: 'a',
          Ma: [
            'ytp-autonav-endscreen-upnext-button',
            'ytp-autonav-endscreen-upnext-play-button',
            b.L('web_modern_buttons') ? 'ytp-autonav-endscreen-upnext-button-rounded' : ''
          ],
          Y: {
            href: '{{url}}',
            role: 'button',
            'aria-label': 'Play next video'
          },
          ya: 'Play now'
        });
        g.M(this, this.playButton);
        this.playButton.Ja(this.B.element);
        this.playButton.Ra('click', this.IS, this);
        this.J.L('web_player_autonav_next_button_renderer') ? (
          this.J.createServerVe(this.playButton.element, this.playButton, !0),
          (b = this.J.getVideoData()) &&
          brb(this, b)
        ) : this.J.createClientVe(this.playButton.element, this, 115130);
        this.D = new g.bv(function () {
          crb(c)
        }, 500);
        g.M(this, this.D);
        this.HS();
        this.T(a, 'autonavvisibility', this.HS);
        this.J.L('web_autonav_color_transition') &&
        (
          this.T(a, 'autonavchange', this.M1),
          this.T(a, 'onAutonavCoundownStarted', this.b9)
        )
      },
      o6 = function (a) {
        var b = a.J.pn(!0, a.J.isFullscreen());
        g.nv(
          a.container.element,
          'ytp-autonav-endscreen-small-mode',
          a.Ag(b)
        );
        g.nv(
          a.container.element,
          'ytp-autonav-endscreen-is-premium',
          !!a.suggestion &&
          !!a.suggestion.wK
        );
        g.nv(
          a.J.getRootNode(),
          'ytp-autonav-endscreen-cancelled-state',
          !a.J.tf()
        );
        g.nv(a.J.getRootNode(), 'countdown-running', a.Rk());
        g.nv(a.container.element, 'ytp-player-content', a.J.tf());
        g.ps(a.overlay.element, {
          width: b.width + 'px'
        });
        if (!a.Rk()) {
          a.J.tf() ? drb(a, Math.round(erb(a) / 1000)) : drb(a);
          b = !!a.suggestion &&
          !!a.suggestion.Wr;
          var c = a.J.tf() ||
          !b;
          g.nv(
            a.container.element,
            'ytp-autonav-endscreen-upnext-alternative-header-only',
            !c &&
            b
          );
          g.nv(
            a.container.element,
            'ytp-autonav-endscreen-upnext-no-alternative-header',
            c &&
            !b
          );
          g.FG(a.B, a.J.tf());
          g.nv(a.element, 'ytp-enable-w2w-color-transitions', frb(a))
        }
      },
      crb = function (a) {
        var b = erb(a),
        c = Math,
        d = c.min;
        var e = a.C ? Date.now() - a.C : 0;
        c = d.call(c, e, b);
        drb(a, Math.ceil((b - c) / 1000));
        500 >= b - c &&
        a.Rk() ? a.select(!0) : a.Rk() &&
        a.D.start()
      },
      erb = function (a) {
        if (a.J.isFullscreen()) {
          var b;
          a = null == (b = a.J.getVideoData()) ? void 0 : b.AB;
          return - 1 === a ||
          void 0 === a ? 8000 : a
        }
        return 0 <= a.J.Fs() ? a.J.Fs() : g.SJ(a.J.U().experiments, 'autoplay_time') ||
        10000
      },
      brb = function (a, b) {
        a.J.L('web_player_autonav_next_button_renderer');
        b = b.i6;
        a.K = null == b ? void 0 : b.navigationEndpoint;
        b = null == b ? void 0 : b.trackingParams;
        a.playButton &&
        b &&
        a.J.setTrackingParams(a.playButton.element, b)
      },
      frb = function (a) {
        var b;
        return !(
          null == (b = a.J.getVideoData()) ||
          !b.watchToWatchTransitionRenderer
        )
      },
      drb = function (a, b) {
        b = void 0 === b ? - 1 : b;
        a = a.j.Ha('ytp-autonav-endscreen-upnext-header');
        g.rf(a);
        if (0 <= b) {
          b = String(b);
          var c = 'Up next in $SECONDS'.match(RegExp('\\$SECONDS', 'gi')) [0],
          d = 'Up next in $SECONDS'.indexOf(c);
          if (0 <= d) {
            a.appendChild(g.pf('Up next in $SECONDS'.slice(0, d)));
            var e = g.of ('span');
            g.hv(e, 'ytp-autonav-endscreen-upnext-header-countdown-number');
            g.zf(e, b);
            a.appendChild(e);
            a.appendChild(g.pf('Up next in $SECONDS'.slice(d + c.length)));
            return
          }
        }
        g.zf(a, 'Up next')
      },
      p6 = function (a, b) {
        g.V.call(
          this,
          {
            I: 'div',
            Ma: [
              'html5-endscreen',
              'ytp-player-content',
              b ||
              'base-endscreen'
            ]
          }
        );
        this.created = !1;
        this.player = a
      },
      q6 = function (a) {
        g.V.call(
          this,
          {
            I: 'div',
            Ma: [
              'ytp-upnext',
              'ytp-player-content'
            ],
            Y: {
              'aria-label': '{{aria_label}}'
            },
            V: [
              {
                I: 'div',
                S: 'ytp-cued-thumbnail-overlay-image',
                Y: {
                  style: '{{background}}'
                }
              },
              {
                I: 'span',
                S: 'ytp-upnext-top',
                V: [
                  {
                    I: 'span',
                    S: 'ytp-upnext-header',
                    ya: 'Up Next'
                  },
                  {
                    I: 'span',
                    S: 'ytp-upnext-title',
                    ya: '{{title}}'
                  },
                  {
                    I: 'span',
                    S: 'ytp-upnext-author',
                    ya: '{{author}}'
                  }
                ]
              },
              {
                I: 'a',
                S: 'ytp-upnext-autoplay-icon',
                Y: {
                  role: 'button',
                  href: '{{url}}',
                  'aria-label': 'Play next video'
                },
                V: [
                  {
                    I: 'svg',
                    Y: {
                      height: '100%',
                      version: '1.1',
                      viewBox: '0 0 72 72',
                      width: '100%'
                    },
                    V: [
                      {
                        I: 'circle',
                        S: 'ytp-svg-autoplay-circle',
                        Y: {
                          cx: '36',
                          cy: '36',
                          fill: '#fff',
                          'fill-opacity': '0.3',
                          r: '31.5'
                        }
                      },
                      {
                        I: 'circle',
                        S: 'ytp-svg-autoplay-ring',
                        Y: {
                          cx: '-36',
                          cy: '36',
                          'fill-opacity': '0',
                          r: '33.5',
                          stroke: '#FFFFFF',
                          'stroke-dasharray': '211',
                          'stroke-dashoffset': '-211',
                          'stroke-width': '4',
                          transform: 'rotate(-90)'
                        }
                      },
                      {
                        I: 'path',
                        S: 'ytp-svg-fill',
                        Y: {
                          d: 'M 24,48 41,36 24,24 V 48 z M 44,24 v 24 h 4 V 24 h -4 z'
                        }
                      }
                    ]
                  }
                ]
              },
              {
                I: 'span',
                S: 'ytp-upnext-bottom',
                V: [
                  {
                    I: 'span',
                    S: 'ytp-upnext-cancel'
                  },
                  {
                    I: 'span',
                    S: 'ytp-upnext-paused',
                    ya: 'Auto-play is paused'
                  }
                ]
              }
            ]
          }
        );
        this.api = a;
        this.cancelButton = null;
        this.G = this.Ha('ytp-svg-autoplay-ring');
        this.C = this.notification = this.j = this.suggestion = null;
        this.D = new g.bv(this.XG, 5000, this);
        this.B = 0;
        var b = this.Ha('ytp-upnext-cancel');
        this.cancelButton = new g.V({
          I: 'button',
          Ma: [
            'ytp-upnext-cancel-button',
            'ytp-button'
          ],
          Y: {
            tabindex: '0',
            'aria-label': 'Cancel auto-play'
          },
          ya: 'Cancel'
        });
        g.M(this, this.cancelButton);
        this.cancelButton.Ra('click', this.O1, this);
        this.cancelButton.Ja(b);
        this.cancelButton &&
        this.api.createClientVe(this.cancelButton.element, this, 115129);
        g.M(this, this.D);
        this.api.createClientVe(this.element, this, 18788);
        b = this.Ha('ytp-upnext-autoplay-icon');
        this.T(b, 'click', this.P1);
        this.api.createClientVe(b, this, 115130);
        this.JS();
        this.T(a, 'autonavvisibility', this.JS);
        this.T(a, 'mdxnowautoplaying', this.M9);
        this.T(a, 'mdxautoplaycanceled', this.N9);
        g.nv(this.element, 'ytp-upnext-mobile', this.api.U().B)
      },
      grb = function (a, b) {
        if (b) return b;
        if (a.api.isFullscreen()) {
          var c;
          a = null == (c = a.api.getVideoData()) ? void 0 : c.AB;
          return - 1 === a ||
          void 0 === a ? 8000 : a
        }
        return 0 <= a.api.Fs() ? a.api.Fs() : g.SJ(a.api.U().experiments, 'autoplay_time') ||
        10000
      },
      hrb = function (a, b) {
        b = grb(a, b);
        var c = Math,
        d = c.min;
        var e = (0, g.WD) () - a.B;
        c = d.call(c, e, b);
        b = 0 === b ? 1 : Math.min(c / b, 1);
        a.G.setAttribute('stroke-dashoffset', '' + - 211 * (b + 1));
        1 <= b &&
        a.Rk() &&
        3 !== a.api.getPresentingPlayerType() ? a.select(!0) : a.Rk() &&
        a.j.start()
      },
      r6 = function (a) {
        p6.call(this, a, 'autonav-endscreen');
        this.overlay = this.videoData = null;
        this.table = new g.V({
          I: 'div',
          S: 'ytp-suggestion-panel',
          V: [
            {
              I: 'div',
              Ma: [
                'ytp-autonav-endscreen-upnext-header',
                'ytp-autonav-endscreen-more-videos'
              ],
              ya: 'More videos'
            }
          ]
        });
        this.N = new g.V({
          I: 'div',
          S: 'ytp-suggestions-container'
        });
        this.videos = [];
        this.C = null;
        this.G = this.K = !1;
        this.B = new n6(this.player);
        g.M(this, this.B);
        this.B.Ja(this.element);
        a.getVideoData().Nf ? this.j = this.B : (
          this.j = new q6(a),
          g.NU(this.player, this.j.element, 4),
          g.M(this, this.j)
        );
        this.overlay = new g.V({
          I: 'div',
          S: 'ytp-autonav-overlay-cancelled-state'
        });
        g.M(this, this.overlay);
        this.overlay.Ja(this.element);
        this.D = new g.kL(this);
        g.M(this, this.D);
        g.M(this, this.table);
        this.table.Ja(this.element);
        this.table.show();
        g.M(this, this.N);
        this.N.Ja(this.table.element);
        this.hide()
      },
      s6 = function (a) {
        var b = a.tf();
        b !== a.G &&
        (
          a.G = b,
          a.player.oa('autonavvisibility'),
          a.G ? (a.B !== a.j && a.B.hide(), a.table.hide()) : (a.B !== a.j && a.B.show(), a.table.show())
        )
      },
      t6 = function (a, b) {
        g.V.call(
          this,
          {
            I: 'button',
            Ma: [
              'ytp-watch-on-youtube-button',
              'ytp-button'
            ],
            ya: '{{content}}'
          }
        );
        this.J = a;
        this.buttonType = this.buttonType = b;
        this.p_();
        2 === this.buttonType &&
        g.jv(this.element, 'ytp-continue-watching-button');
        this.Ra('click', this.onClick);
        this.Ra('videodatachange', this.p_);
        g.FG(this, !0)
      },
      u6 = function (a, b) {
        p6.call(this, a, 'embeds-lite-endscreen');
        this.J = a;
        this.Se = b;
        this.J.createClientVe(this.element, this, 156943);
        this.watchButton = new t6(a, 2);
        g.M(this, this.watchButton);
        this.watchButton.Ja(this.element);
        this.hide()
      },
      irb = function (a) {
        p6.call(this, a, 'subscribecard-endscreen');
        this.j = new g.V({
          I: 'div',
          S: 'ytp-subscribe-card',
          V: [
            {
              I: 'img',
              S: 'ytp-author-image',
              Y: {
                src: '{{profilePicture}}'
              }
            },
            {
              I: 'div',
              S: 'ytp-subscribe-card-right',
              V: [
                {
                  I: 'div',
                  S: 'ytp-author-name',
                  ya: '{{author}}'
                },
                {
                  I: 'div',
                  S: 'html5-subscribe-button-container'
                }
              ]
            }
          ]
        });
        g.M(this, this.j);
        this.j.Ja(this.element);
        var b = a.getVideoData();
        this.subscribeButton = new g.IW(
          'Subscribe',
          null,
          'Unsubscribe',
          null,
          !0,
          !1,
          b.Bl,
          b.subscribed,
          'trailer-endscreen',
          null,
          a,
          !1
        );
        g.M(this, this.subscribeButton);
        this.subscribeButton.Ja(this.j.Ha('html5-subscribe-button-container'));
        this.T(a, 'videodatachange', this.Qa);
        this.Qa();
        this.hide()
      },
      v6 = function (a) {
        var b = a.U(),
        c = g.iL ||
        g.sS ? {
          style: 'will-change: opacity'
        }
         : void 0,
        d = b.D,
        e = [
          'ytp-videowall-still'
        ];
        b.B &&
        e.push('ytp-videowall-show-text');
        g.V.call(
          this,
          {
            I: 'a',
            Ma: e,
            Y: {
              href: '{{url}}',
              target: d ? b.W : '',
              'aria-label': '{{aria_label}}',
              'data-is-live': '{{is_live}}',
              'data-is-list': '{{is_list}}',
              'data-is-mix': '{{is_mix}}'
            },
            V: [
              {
                I: 'div',
                S: 'ytp-videowall-still-image',
                Y: {
                  style: '{{background}}'
                }
              },
              {
                I: 'span',
                S: 'ytp-videowall-still-info',
                Y: {
                  'aria-hidden': 'true'
                },
                V: [
                  {
                    I: 'span',
                    S: 'ytp-videowall-still-info-bg',
                    V: [
                      {
                        I: 'span',
                        S: 'ytp-videowall-still-info-content',
                        Y: c,
                        V: [
                          {
                            I: 'span',
                            S: 'ytp-videowall-still-info-title',
                            ya: '{{title}}'
                          },
                          {
                            I: 'span',
                            S: 'ytp-videowall-still-info-author',
                            ya: '{{author_and_views}}'
                          },
                          {
                            I: 'span',
                            S: 'ytp-videowall-still-info-live',
                            ya: 'Live'
                          },
                          {
                            I: 'span',
                            S: 'ytp-videowall-still-info-duration',
                            ya: '{{duration}}'
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                I: 'span',
                Ma: [
                  'ytp-videowall-still-listlabel-regular',
                  'ytp-videowall-still-listlabel'
                ],
                Y: {
                  'aria-hidden': 'true'
                },
                V: [
                  {
                    I: 'span',
                    S: 'ytp-videowall-still-listlabel-icon'
                  },
                  'Playlist',
                  {
                    I: 'span',
                    S: 'ytp-videowall-still-listlabel-length',
                    V: [
                      ' (',
                      {
                        I: 'span',
                        ya: '{{playlist_length}}'
                      },
                      ')'
                    ]
                  }
                ]
              },
              {
                I: 'span',
                Ma: [
                  'ytp-videowall-still-listlabel-mix',
                  'ytp-videowall-still-listlabel'
                ],
                Y: {
                  'aria-hidden': 'true'
                },
                V: [
                  {
                    I: 'span',
                    S: 'ytp-videowall-still-listlabel-mix-icon'
                  },
                  'Mix',
                  {
                    I: 'span',
                    S: 'ytp-videowall-still-listlabel-length',
                    ya: ' (50+)'
                  }
                ]
              }
            ]
          }
        );
        this.suggestion = null;
        this.B = d;
        this.api = a;
        this.j = new g.kL(this);
        g.M(this, this.j);
        this.Ra('click', this.onClick);
        this.Ra('keypress', this.onKeyPress);
        this.j.T(a, 'videodatachange', this.onVideoDataChange);
        a.createServerVe(this.element, this);
        this.onVideoDataChange()
      },
      w6 = function (a) {
        p6.call(this, a, 'videowall-endscreen');
        var b = this;
        this.J = a;
        this.C = 0;
        this.stills = [];
        this.D = this.videoData = null;
        this.G = this.N = !1;
        this.W = null;
        this.B = new g.kL(this);
        g.M(this, this.B);
        this.K = new g.bv(function () {
          g.jv(b.element, 'ytp-show-tiles')
        }, 0);
        g.M(this, this.K);
        var c = new g.V({
          I: 'button',
          Ma: [
            'ytp-button',
            'ytp-endscreen-previous'
          ],
          Y: {
            'aria-label': 'Previous'
          },
          V: [
            g.LG()
          ]
        });
        g.M(this, c);
        c.Ja(this.element);
        c.Ra('click', this.T1, this);
        this.table = new g.CG({
          I: 'div',
          S: 'ytp-endscreen-content'
        });
        g.M(this, this.table);
        this.table.Ja(this.element);
        c = new g.V({
          I: 'button',
          Ma: [
            'ytp-button',
            'ytp-endscreen-next'
          ],
          Y: {
            'aria-label': 'Next'
          },
          V: [
            g.MG()
          ]
        });
        g.M(this, c);
        c.Ja(this.element);
        c.Ra('click', this.S1, this);
        a.getVideoData().Nf ? this.j = new n6(a, !0) : this.j = new q6(a);
        g.M(this, this.j);
        g.NU(this.player, this.j.element, 4);
        a.createClientVe(this.element, this, 158789);
        this.hide()
      },
      x6 = function (a) {
        return g.OU(a.player) &&
        a.vC() &&
        !a.D
      },
      y6 = function (a) {
        var b = a.tf();
        b !== a.N &&
        (a.N = b, a.player.oa('autonavvisibility'))
      },
      z6 = function (a) {
        p6.call(this, a, 'watch-again-on-youtube-endscreen');
        this.watchButton = new t6(a, 1);
        g.M(this, this.watchButton);
        this.watchButton.Ja(this.element);
        g.sfb(a) &&
        (
          this.j = new g.B2(a),
          g.M(this, this.j),
          this.B = new g.V({
            I: 'div',
            Ma: [
              'ytp-watch-again-on-youtube-endscreen-more-videos-container'
            ],
            Y: {
              tabIndex: '-1'
            },
            V: [
              this.j
            ]
          }),
          g.M(this, this.B),
          this.j.Ja(this.B.element),
          this.B.Ja(this.element)
        );
        a.createClientVe(this.element, this, 156914);
        this.hide()
      },
      mrb = function (a) {
        g.aW.call(this, a);
        var b = this;
        this.endScreen = null;
        this.B = this.j = this.C = this.D = !1;
        this.listeners = new g.kL(this);
        g.M(this, this.listeners);
        var c = a.U(),
        d = a.getVideoData();
        d = d &&
        0 !== d.limitedPlaybackDurationInSeconds;
        g.WC(g.BS(c)) &&
        d &&
        !g.KU(a) ? (this.B = !0, this.endScreen = new u6(a, g.BU(a))) : a.Xc() ? this.endScreen = new z6(a) : jrb(a) ? (
          this.D = !0,
          krb(this),
          this.j ? this.endScreen = new r6(a) : this.endScreen = new w6(a)
        ) : c.Rg ? this.endScreen = new irb(a) : this.endScreen = new p6(a);
        g.M(this, this.endScreen);
        g.NU(a, this.endScreen.element, 4);
        lrb(this);
        this.listeners.T(a, 'videodatachange', this.onVideoDataChange, this);
        this.listeners.T(a, g.zK('endscreen'), function (e) {
          b.onCueRangeEnter(e)
        });
        this.listeners.T(a, g.AK('endscreen'), function (e) {
          b.onCueRangeExit(e)
        })
      },
      krb = function (a) {
        var b = a.player.getVideoData();
        if (!b || a.j === b.Dl && a.C === b.Nf) return !1;
        a.j = b.Dl;
        a.C = b.Nf;
        return !0
      },
      jrb = function (a) {
        a = a.U();
        return a.Wd &&
        !a.Rg
      },
      lrb = function (a) {
        a.player.yf('endscreen');
        var b = a.player.getVideoData();
        b = new g.yK(
          Math.max(1000 * (b.lengthSeconds - 10), 0),
          2251799813685248,
          {
            id: 'preload',
            namespace: 'endscreen'
          }
        );
        var c = new g.yK(
          2251799813685248,
          2251799813685248,
          {
            id: 'load',
            priority: 8,
            namespace: 'endscreen'
          }
        );
        a.player.rf([b,
        c])
      };
      g.GU.prototype.Fs = g.da(16, function () {
        return this.app.Fs()
      });
      g.i1.prototype.Fs = g.da(15, function () {
        return this.getVideoData().uU
      });
      g.CU.prototype.yr = g.da(14, function (a) {
        this.oi().yr(a)
      });
      g.gX.prototype.yr = g.da(13, function (a) {
        this.j !== a &&
        (this.j = a, this.Qa())
      });
      g.nY.prototype.yr = g.da(
        12,
        function (a) {
          this.overflowButton &&
          this.overflowButton.yr(a)
        }
      );
      g.CU.prototype.zr = g.da(11, function (a) {
        this.oi().zr(a)
      });
      g.lX.prototype.zr = g.da(10, function (a) {
        this.j !== a &&
        (this.j = a, this.Qa())
      });
      g.nY.prototype.zr = g.da(9, function (a) {
        this.shareButton &&
        this.shareButton.zr(a)
      });
      g.CU.prototype.ZA = g.da(8, function (a) {
        this.oi().ZA(a)
      });
      g.BW.prototype.ZA = g.da(7, function (a) {
        this.uQ !== a &&
        (this.uQ = a, this.Xp())
      });
      g.CU.prototype.YA = g.da(6, function (a) {
        this.oi().YA(a)
      });
      g.nY.prototype.YA = g.da(5, function (a) {
        this.tQ !== a &&
        (this.tQ = a, this.Wp())
      });
      g.w(m6, g.V);
      m6.prototype.select = function () {
        this.J.Ao(
          this.suggestion.videoId,
          this.suggestion.sessionData,
          this.suggestion.playlistId,
          void 0,
          void 0,
          this.suggestion.QC ||
          void 0
        ) &&
        this.J.logClick(this.element)
      };
      m6.prototype.onClick = function (a) {
        g.iV(a, this.J, this.j, this.suggestion.sessionData || void 0) &&
        this.select()
      };
      m6.prototype.onKeyPress = function (a) {
        switch (a.keyCode) {
          case 13:
          case 32:
            a.defaultPrevented ||
            (this.select(), a.preventDefault())
        }
      };
      g.w(n6, g.V);
      g.k = n6.prototype;
      g.k.iG = function (a) {
        this.suggestion !== a &&
        (
          this.suggestion = a,
          l6(this.j, a),
          this.playButton.updateValue('url', this.suggestion.Nk()),
          o6(this)
        )
      };
      g.k.Rk = function () {
        return 0 < this.C
      };
      g.k.hB = function () {
        this.Rk() ||
        (
          this.C = Date.now(),
          crb(this),
          arb(this.J, erb(this)),
          g.nv(this.J.getRootNode(), 'countdown-running', this.Rk())
        )
      };
      g.k.Fw = function () {
        this.Sp();
        crb(this);
        var a = this.j.Ha('ytp-autonav-endscreen-upnext-header');
        a &&
        g.zf(a, 'Up next')
      };
      g.k.Sp = function () {
        this.Rk() &&
        (this.D.stop(), this.C = 0)
      };
      g.k.select = function (a) {
        this.J.nextVideo(!1, void 0 === a ? !1 : a);
        this.Sp()
      };
      g.k.IS = function (a) {
        g.iV(a, this.J) &&
        (
          a.currentTarget === this.playButton.element ? this.J.logClick(this.playButton.element) : a.currentTarget === this.j.Ha('ytp-autonav-endscreen-link-container') &&
          (
            a = this.j.Ha('ytp-autonav-endscreen-link-container'),
            this.J.logVisibility(a, !0),
            this.J.logClick(a)
          ),
          this.J.L('web_player_autonav_next_button_renderer') &&
          this.K ? (this.J.jb('innertubeCommand', this.K), this.Sp()) : this.select()
        )
      };
      g.k.N1 = function () {
        this.J.logClick(this.cancelButton.element);
        g.IU(this.J, !0);
        this.G &&
        this.J.jb('innertubeCommand', this.G)
      };
      g.k.onVideoDataChange = function (a, b) {
        this.J.L('web_player_autonav_next_button_renderer') &&
        brb(this, b);
        var c;
        this.G = null == (c = b.P5) ? void 0 : c.command
      };
      g.k.b9 = function (a) {
        if (frb(this)) {
          var b = this.J.getVideoData().watchToWatchTransitionRenderer,
          c = null == b ? void 0 : b.fromColorPaletteDark;
          b = null == b ? void 0 : b.toColorPaletteDark;
          if (c && b) {
            var d = this.element;
            d.style.setProperty('--w2w-start-background-color', g.GH(c.surgeColor));
            d.style.setProperty('--w2w-start-primary-text-color', g.GH(c.primaryTitleColor));
            d.style.setProperty(
              '--w2w-start-secondary-text-color',
              g.GH(c.secondaryTitleColor)
            );
            d.style.setProperty('--w2w-end-background-color', g.GH(b.surgeColor));
            d.style.setProperty('--w2w-end-primary-text-color', g.GH(b.primaryTitleColor));
            d.style.setProperty('--w2w-end-secondary-text-color', g.GH(b.secondaryTitleColor));
            d.style.setProperty('--w2w-animation-duration', a + 'ms')
          }
          g.nv(this.element, 'ytp-w2w-animate', !0)
        }
      };
      g.k.M1 = function (a) {
        this.J.L('web_autonav_color_transition') &&
        2 !== a &&
        g.nv(this.element, 'ytp-w2w-animate', !1)
      };
      g.k.HS = function () {
        var a = this.J.tf();
        this.N &&
        this.Ib !== a &&
        g.FG(this, a);
        o6(this);
        this.J.logVisibility(this.container.element, a);
        this.J.logVisibility(this.cancelButton.element, a);
        this.J.logVisibility(this.j.Ha('ytp-autonav-endscreen-link-container'), a);
        this.J.logVisibility(this.playButton.element, a)
      };
      g.k.Ag = function (a) {
        return 400 > a.width ||
        459 > a.height
      };
      g.w(p6, g.V);
      g.k = p6.prototype;
      g.k.create = function () {
        this.created = !0
      };
      g.k.destroy = function () {
        this.created = !1
      };
      g.k.vC = function () {
        return !1
      };
      g.k.tf = function () {
        return !1
      };
      g.k.FX = function () {
        return !1
      };
      g.w(q6, g.V);
      g.k = q6.prototype;
      g.k.XG = function () {
        this.notification &&
        (
          this.D.stop(),
          this.Pc(this.C),
          this.C = null,
          this.notification.close(),
          this.notification = null
        )
      };
      g.k.iG = function (a) {
        this.suggestion = a;
        l6(this, a, 'hqdefault.jpg')
      };
      g.k.JS = function () {
        g.FG(this, this.api.tf());
        this.api.logVisibility(this.element, this.api.tf());
        this.api.logVisibility(this.Ha('ytp-upnext-autoplay-icon'), this.api.tf());
        this.cancelButton &&
        this.api.logVisibility(this.cancelButton.element, this.api.tf())
      };
      g.k.V9 = function () {
        window.focus();
        this.XG()
      };
      g.k.hB = function (a) {
        var b = this;
        this.Rk() ||
        (
          g.eF('a11y-announce', 'Up Next ' + this.suggestion.title),
          this.B = (0, g.WD) (),
          this.j = new g.bv(function () {
            hrb(b, a)
          }, 25),
          hrb(this, a),
          arb(this.api, grb(this, a))
        );
        g.lv(this.element, 'ytp-upnext-autoplay-paused')
      };
      g.k.hide = function () {
        g.V.prototype.hide.call(this)
      };
      g.k.Rk = function () {
        return !!this.j
      };
      g.k.Fw = function () {
        this.Sp();
        this.B = (0, g.WD) ();
        hrb(this);
        g.jv(this.element, 'ytp-upnext-autoplay-paused')
      };
      g.k.Sp = function () {
        this.Rk() &&
        (this.j.dispose(), this.j = null)
      };
      g.k.select = function (a) {
        a = void 0 === a ? !1 : a;
        if (
          this.api.U().L('autonav_notifications') &&
          a &&
          window.Notification &&
          'function' === typeof document.hasFocus
        ) {
          var b = Notification.permission;
          'default' === b ? Notification.requestPermission() : 'granted' !== b ||
          document.hasFocus() ||
          (
            this.XG(),
            this.notification = new Notification(
              'Up Next',
              {
                body: this.suggestion.title,
                icon: this.suggestion.Xg()
              }
            ),
            this.C = this.T(this.notification, 'click', this.V9),
            this.D.start()
          )
        }
        this.Sp();
        this.api.nextVideo(!1, a)
      };
      g.k.P1 = function (a) {
        !g.yf(this.cancelButton.element, a.target) &&
        g.iV(a, this.api) &&
        (
          this.api.tf() &&
          this.api.logClick(this.Ha('ytp-upnext-autoplay-icon')),
          this.select()
        )
      };
      g.k.O1 = function () {
        this.api.tf() &&
        this.cancelButton &&
        this.api.logClick(this.cancelButton.element);
        g.IU(this.api, !0)
      };
      g.k.M9 = function (a) {
        this.api.getPresentingPlayerType();
        this.show();
        this.hB(a)
      };
      g.k.N9 = function () {
        this.api.getPresentingPlayerType();
        this.Sp();
        this.hide()
      };
      g.k.xa = function () {
        this.Sp();
        this.XG();
        g.V.prototype.xa.call(this)
      };
      g.w(r6, p6);
      g.k = r6.prototype;
      g.k.create = function () {
        p6.prototype.create.call(this);
        this.D.T(this.player, 'appresize', this.IB);
        this.D.T(this.player, 'onVideoAreaChange', this.IB);
        this.D.T(this.player, 'videodatachange', this.onVideoDataChange);
        this.D.T(this.player, 'autonavchange', this.KS);
        this.D.T(this.player, 'onAutonavCancelled', this.Q1);
        this.onVideoDataChange()
      };
      g.k.show = function () {
        p6.prototype.show.call(this);
        (this.K || this.C && this.C !== this.videoData.clientPlaybackNonce) &&
        g.IU(this.player, !1);
        g.OU(this.player) &&
        this.vC() &&
        !this.C ? (
          s6(this),
          2 === this.videoData.autonavState ? 3 === this.player.getVisibilityState() ? this.j.select(!0) : this.j.hB() : 3 === this.videoData.autonavState &&
          this.j.Fw()
        ) : (g.IU(this.player, !0), s6(this));
        this.IB()
      };
      g.k.hide = function () {
        p6.prototype.hide.call(this);
        this.j.Fw();
        s6(this)
      };
      g.k.IB = function () {
        var a = this.player.pn(!0, this.player.isFullscreen());
        s6(this);
        o6(this.B);
        g.nv(this.element, 'ytp-autonav-cancelled-small-mode', this.Ag(a));
        g.nv(this.element, 'ytp-autonav-cancelled-tiny-mode', this.AI(a));
        g.nv(
          this.element,
          'ytp-autonav-cancelled-mini-mode',
          400 >= a.width ||
          360 >= a.height
        );
        this.overlay &&
        g.ps(this.overlay.element, {
          width: a.width + 'px'
        });
        if (!this.G) for (a = 0; a < this.videos.length; a++) g.nv(
          this.videos[a].element,
          'ytp-suggestion-card-with-margin',
          1 === a % 2
        )
      };
      g.k.onVideoDataChange = function () {
        var a = this.player.getVideoData();
        if (this.videoData !== a && a) {
          this.videoData = a;
          if (
            (a = this.videoData.suggestions) &&
            a.length ||
            this.player.L('web_player_autonav_empty_suggestions_fix')
          ) {
            var b = g.GT(this.videoData);
            b &&
            (this.j.iG(b), this.j !== this.B && this.B.iG(b))
          }
          if (a && a.length) for (b = 0; b < nrb.length; ++b) {
            var c = nrb[b];
            if (a && a[c]) {
              this.videos[b] = new m6(this.player);
              var d = this.videos[b];
              c = a[c];
              d.suggestion !== c &&
              (d.suggestion = c, l6(d, c));
              g.M(this, this.videos[b]);
              this.videos[b].Ja(this.N.element)
            }
          }
          this.IB()
        }
      };
      g.k.KS = function (a) {
        1 === a ? (
          this.K = !1,
          this.C = this.videoData.clientPlaybackNonce,
          this.j.Sp(),
          this.Ib &&
          this.IB()
        ) : (this.K = !0, this.tf() && (2 === a ? this.j.hB() : 3 === a && this.j.Fw()))
      };
      g.k.Q1 = function (a) {
        a ? this.KS(1) : (this.C = null, this.K = !1)
      };
      g.k.vC = function () {
        return 1 !== this.videoData.autonavState
      };
      g.k.Ag = function (a) {
        return (910 > a.width || 459 > a.height) &&
        !this.AI(a) &&
        !(400 >= a.width || 360 >= a.height)
      };
      g.k.AI = function (a) {
        return 800 > a.width &&
        !(400 >= a.width || 360 >= a.height)
      };
      g.k.tf = function () {
        return this.Ib &&
        g.OU(this.player) &&
        this.vC() &&
        !this.C
      };
      var nrb = [
        1,
        3,
        2,
        4
      ];
      g.w(t6, g.V);
      g.k = t6.prototype;
      g.k.p_ = function () {
        switch (this.buttonType) {
          case 1:
            var a = 'Watch again on YouTube';
            var b = 156915;
            break;
          case 2:
            a = 'Continue watching on YouTube';
            b = 156942;
            break;
          default:
            a = 'Continue watching on YouTube',
            b = 156942
        }
        this.update({
          content: a
        });
        this.J.hasVe(this.element) &&
        this.J.destroyVe(this.element);
        this.J.createClientVe(this.element, this, b)
      };
      g.k.onClick = function (a) {
        this.J.L(
          'web_player_log_click_before_generating_ve_conversion_params'
        ) &&
        this.J.logClick(this.element);
        g.jV(this.getVideoUrl(), this.J, a);
        this.J.L(
          'web_player_log_click_before_generating_ve_conversion_params'
        ) ||
        this.J.logClick(this.element)
      };
      g.k.getVideoUrl = function () {
        var a = !0;
        switch (this.buttonType) {
          case 1:
            a = !0;
            break;
          case 2:
            a = !1
        }
        a = this.J.getVideoUrl(a, !1, !1, !0);
        var b = this.J.U();
        if (g.tS(b)) {
          var c = {};
          g.tS(b) &&
          g.vU(this.J, 'addEmbedsConversionTrackingParams', [
            c
          ]);
          a: {
            switch (this.buttonType) {
              case 2:
                b = 'emb_ytp_continue_watching';
                break a
            }
            b = 'emb_ytp_watch_again'
          }
          g.QP(c, b);
          a = g.Bm(a, c)
        }
        return a
      };
      g.k.logVisibility = function () {
        this.J.logVisibility(this.element, this.Ib && this.Z)
      };
      g.k.show = function () {
        g.V.prototype.show.call(this);
        this.logVisibility()
      };
      g.k.hide = function () {
        g.V.prototype.hide.call(this);
        this.logVisibility()
      };
      g.k.Ic = function (a) {
        g.V.prototype.Ic.call(this, a);
        this.logVisibility()
      };
      g.w(u6, p6);
      u6.prototype.show = function () {
        3 !== this.player.getPlayerState() &&
        (
          p6.prototype.show.call(this),
          this.Se.YA(!0),
          this.Se.zr(!0),
          this.J.U().Je ||
          this.Se.yr(!0),
          this.J.logVisibility(this.element, !0),
          this.watchButton.Ic(!0)
        )
      };
      u6.prototype.hide = function () {
        p6.prototype.hide.call(this);
        this.Se.YA(!1);
        this.Se.zr(!1);
        this.Se.yr(!1);
        this.J.logVisibility(this.element, !1);
        this.watchButton.Ic(!1)
      };
      g.w(irb, p6);
      irb.prototype.Qa = function () {
        var a = this.player.getVideoData();
        this.j.update({
          profilePicture: a.profilePicture,
          author: a.author
        });
        this.subscribeButton.channelId = a.Bl;
        var b = this.subscribeButton;
        a.subscribed ? b.j() : b.B()
      };
      g.w(v6, g.V);
      v6.prototype.select = function () {
        this.api.Ao(
          this.suggestion.videoId,
          this.suggestion.sessionData,
          this.suggestion.playlistId,
          void 0,
          void 0,
          this.suggestion.QC ||
          void 0
        ) &&
        this.api.logClick(this.element)
      };
      v6.prototype.onClick = function (a) {
        if (
          g.tS(this.api.U()) &&
          this.api.L(
            'web_player_log_click_before_generating_ve_conversion_params'
          )
        ) {
          this.api.logClick(this.element);
          var b = this.suggestion.Nk(),
          c = {};
          g.xTa(this.api, c, 'emb_rel_end');
          b = g.Bm(b, c);
          g.jV(b, this.api, a)
        } else g.iV(a, this.api, this.B, this.suggestion.sessionData || void 0) &&
        this.select()
      };
      v6.prototype.onKeyPress = function (a) {
        switch (a.keyCode) {
          case 13:
          case 32:
            a.defaultPrevented ||
            (this.select(), a.preventDefault())
        }
      };
      v6.prototype.onVideoDataChange = function () {
        var a = this.api.getVideoData(),
        b = this.api.U();
        this.B = a.Hf ? !1 : b.D
      };
      g.w(w6, p6);
      g.k = w6.prototype;
      g.k.create = function () {
        p6.prototype.create.call(this);
        var a = this.player.getVideoData();
        a &&
        (this.videoData = a);
        this.bq();
        this.B.T(this.player, 'appresize', this.bq);
        this.B.T(this.player, 'onVideoAreaChange', this.bq);
        this.B.T(this.player, 'videodatachange', this.onVideoDataChange);
        this.B.T(this.player, 'autonavchange', this.pL);
        this.B.T(this.player, 'onAutonavCancelled', this.R1);
        a = this.videoData.autonavState;
        a !== this.W &&
        this.pL(a);
        this.B.T(this.element, 'transitionend', this.naa)
      };
      g.k.destroy = function () {
        g.kD(this.B);
        g.wb(this.stills);
        this.stills = [];
        p6.prototype.destroy.call(this);
        g.lv(this.element, 'ytp-show-tiles');
        this.K.stop();
        this.W = this.videoData.autonavState
      };
      g.k.vC = function () {
        return 1 !== this.videoData.autonavState
      };
      g.k.show = function () {
        var a = this.Ib;
        p6.prototype.show.call(this);
        g.lv(this.element, 'ytp-show-tiles');
        this.player.U().B ? g.dv(this.K) : this.K.start();
        (this.G || this.D && this.D !== this.videoData.clientPlaybackNonce) &&
        g.IU(this.player, !1);
        x6(this) ? (
          y6(this),
          2 === this.videoData.autonavState ? 3 === this.player.getVisibilityState() ? this.j.select(!0) : this.j.hB() : 3 === this.videoData.autonavState &&
          this.j.Fw()
        ) : (g.IU(this.player, !0), y6(this));
        a !== this.Ib &&
        this.player.logVisibility(this.element, !0)
      };
      g.k.hide = function () {
        var a = this.Ib;
        p6.prototype.hide.call(this);
        this.j.Fw();
        y6(this);
        a !== this.Ib &&
        this.player.logVisibility(this.element, !1)
      };
      g.k.naa = function (a) {
        a.target === this.element &&
        this.bq()
      };
      g.k.bq = function () {
        var a,
        b,
        c,
        d;
        var e = (
          null == (a = this.videoData) ? 0 : null == (b = a.suggestions) ? 0 : b.length
        ) ? null == (c = this.videoData) ? void 0 : c.suggestions : [
          null == (d = this.videoData) ? void 0 : g.GT(d)
        ];
        if (e.length) {
          g.jv(this.element, 'ytp-endscreen-paginate');
          var f = this.J.pn(!0, this.J.isFullscreen());
          if (a = g.BU(this.J)) a = a.ph() ? 48 : 32,
          f.width -= 2 * a;
          var h = f.width / f.height;
          d = 96 / 54;
          b = a = 2;
          var l = Math.max(f.width / 96, 2),
          m = Math.max(f.height / 54, 2);
          c = e.length;
          var n = Math.pow(2, 2);
          var p = c * n + (Math.pow(2, 2) - n);
          p += Math.pow(2, 2) -
          n;
          for (p -= n; 0 < p && (a < l || b < m); ) {
            var q = a / 2,
            r = b / 2,
            t = a <= l - 2 &&
            p >= r * n,
            v = b <= m - 2 &&
            p >= q * n;
            if ((q + 1) / r * d / h > h / (q / (r + 1) * d) && v) p -= q * n,
            b += 2;
             else if (t) p -= r * n,
            a += 2;
             else if (v) p -= q * n,
            b += 2;
             else break
          }
          d = !1;
          p >= 3 * n &&
          6 >= c * n - p &&
          (4 <= b || 4 <= a) &&
          (d = !0);
          n = 96 * a;
          p = 54 * b;
          h = n / p < h ? f.height / p : f.width / n;
          h = Math.min(h, 2);
          n = Math.floor(Math.min(f.width, n * h));
          p = Math.floor(Math.min(f.height, p * h));
          f = this.table.element;
          f.ariaLive = 'polite';
          g.As(f, n, p);
          g.ps(f, {
            marginLeft: n / - 2 + 'px',
            marginTop: p / - 2 + 'px'
          });
          this.j.iG(g.GT(this.videoData));
          this.j instanceof n6 &&
          o6(this.j);
          g.nv(this.element, 'ytp-endscreen-takeover', x6(this));
          y6(this);
          n += 4;
          p += 4;
          h = 0;
          f.ariaBusy = 'true';
          for (l = 0; l < a; l++) for (m = 0; m < b; m++) if (
            q = h,
            t = 0,
            d &&
            l >= a - 2 &&
            m >= b - 2 ? t = 1 : 0 === m % 2 &&
            0 === l % 2 &&
            (2 > m && 2 > l ? 0 === m &&
            0 === l &&
            (t = 2) : t = 2),
            q = g.xe(q + this.C, c),
            0 !== t
          ) {
            r = this.stills[h];
            r ||
            (
              r = new v6(this.player),
              this.stills[h] = r,
              f.appendChild(r.element)
            );
            v = Math.floor(p * m / b);
            var x = Math.floor(n * l / a),
            B = Math.floor(p * (m + t) / b) - v - 4,
            E = Math.floor(n * (l + t) / a) - x - 4;
            g.ws(r.element, x, v);
            g.As(r.element, E, B);
            g.ps(r.element, 'transitionDelay', (m + l) / 20 + 's');
            g.nv(r.element, 'ytp-videowall-still-mini', 1 === t);
            g.nv(r.element, 'ytp-videowall-still-large', 2 < t);
            t = Math.max(E, B);
            g.nv(r.element, 'ytp-videowall-still-round-large', 256 <= t);
            g.nv(r.element, 'ytp-videowall-still-round-medium', 96 < t && 256 > t);
            g.nv(r.element, 'ytp-videowall-still-round-small', 96 >= t);
            q = e[q];
            r.suggestion !== q &&
            (
              r.suggestion = q,
              t = r.api.U(),
              v = g.iv(r.element, 'ytp-videowall-still-large') ? 'hqdefault.jpg' : 'mqdefault.jpg',
              l6(r, q, v),
              g.tS(t) &&
              !r.api.L(
                'web_player_log_click_before_generating_ve_conversion_params'
              ) &&
              (
                t = q.Nk(),
                v = {},
                g.vU(r.api, 'addEmbedsConversionTrackingParams', [
                  v
                ]),
                t = g.Bm(t, g.QP(v, 'emb_rel_end')),
                r.updateValue('url', t)
              ),
              (q = (q = q.sessionData) && q.itct) &&
              r.api.setTrackingParams(r.element, q)
            );
            h++
          }
          f.ariaBusy = 'false';
          g.nv(this.element, 'ytp-endscreen-paginate', h < c);
          for (e = this.stills.length - 1; e >= h; e--) a = this.stills[e],
          g.tf(a.element),
          g.vb(a);
          this.stills.length = h
        }
      };
      g.k.onVideoDataChange = function () {
        var a = this.player.getVideoData();
        this.videoData !== a &&
        (this.C = 0, this.videoData = a, this.bq())
      };
      g.k.S1 = function () {
        this.C += this.stills.length;
        this.bq()
      };
      g.k.T1 = function () {
        this.C -= this.stills.length;
        this.bq()
      };
      g.k.FX = function () {
        return this.j.Rk()
      };
      g.k.pL = function (a) {
        1 === a ? (
          this.G = !1,
          this.D = this.videoData.clientPlaybackNonce,
          this.j.Sp(),
          this.Ib &&
          this.bq()
        ) : (
          this.G = !0,
          this.Ib &&
          x6(this) &&
          (2 === a ? this.j.hB() : 3 === a && this.j.Fw())
        )
      };
      g.k.R1 = function (a) {
        if (a) {
          for (a = 0; a < this.stills.length; a++) this.J.logVisibility(this.stills[a].element, !0);
          this.pL(1)
        } else this.D = null,
        this.G = !1;
        this.bq()
      };
      g.k.tf = function () {
        return this.Ib &&
        x6(this)
      };
      g.w(z6, p6);
      z6.prototype.ED = function () {
        var a;
        return null == (a = this.j) ? void 0 : a.ED()
      };
      z6.prototype.show = function () {
        if (3 !== this.player.getPlayerState()) {
          p6.prototype.show.call(this);
          var a = this.B;
          if (a) {
            var b = this.j.ED();
            g.nv(this.element, 'ytp-shorts-branded-ui', b);
            b ? a.show() : a.hide()
          }
          var c;
          null == (c = g.BU(this.player)) ||
          c.ZA(!0);
          this.player.logVisibility(this.element, !0);
          this.watchButton.Ic(!0)
        }
      };
      z6.prototype.hide = function () {
        p6.prototype.hide.call(this);
        var a;
        null == (a = g.BU(this.player)) ||
        a.ZA(!1);
        this.player.logVisibility(this.element, !1);
        this.watchButton.Ic(!1)
      };
      g.w(mrb, g.aW);
      g.k = mrb.prototype;
      g.k.Tt = function () {
        var a = this.player.getVideoData(),
        b = a.mutedAutoplay;
        if ((this.player.Xc() || this.B) && !b) return !0;
        var c;
        var d = !!(
          (null == a ? 0 : g.GT(a)) ||
          (null == a ? 0 : null == (c = a.suggestions) ? 0 : c.length)
        );
        d = !jrb(this.player) ||
        d;
        a = a.wj;
        c = this.player.dD();
        return d &&
        !a &&
        !c &&
        !b
      };
      g.k.tf = function () {
        return this.endScreen.tf()
      };
      g.k.L7 = function () {
        return this.tf() ? this.endScreen.FX() : !1
      };
      g.k.xa = function () {
        this.player.yf('endscreen');
        g.aW.prototype.xa.call(this)
      };
      g.k.load = function () {
        var a = this.player.getVideoData();
        var b = a.transitionEndpointAtEndOfStream;
        if (b && b.videoId) {
          var c = this.player.Cb().Ge.get('heartbeat'),
          d = g.GT(a);
          !d ||
          b.videoId !== d.videoId ||
          a.vS ? (
            this.player.Ao(b.videoId, void 0, void 0, !0, !0, b),
            c &&
            c.LI(
              'HEARTBEAT_ACTION_TRIGGER_AT_STREAM_END',
              'HEARTBEAT_ACTION_TRANSITION_REASON_HAS_NEW_STREAM_TRANSITION_ENDPOINT'
            ),
            a = !0
          ) : a = !1
        } else a = !1;
        a ||
        (g.aW.prototype.load.call(this), this.endScreen.show())
      };
      g.k.unload = function () {
        g.aW.prototype.unload.call(this);
        this.endScreen.hide();
        this.endScreen.destroy()
      };
      g.k.onCueRangeEnter = function (a) {
        this.Tt() &&
        (
          this.endScreen.created ||
          this.endScreen.create(),
          'load' === a.getId() &&
          this.load()
        )
      };
      g.k.onCueRangeExit = function (a) {
        'load' === a.getId() &&
        this.loaded &&
        this.unload()
      };
      g.k.onVideoDataChange = function () {
        lrb(this);
        this.D &&
        krb(this) &&
        (
          this.endScreen &&
          (
            this.endScreen.hide(),
            this.endScreen.created &&
            this.endScreen.destroy(),
            this.endScreen.dispose()
          ),
          this.j ? this.endScreen = new r6(this.player) : this.endScreen = new w6(this.player),
          g.M(this, this.endScreen),
          g.NU(this.player, this.endScreen.element, 4)
        )
      };
      g.$V('endscreen', mrb);
    }
  ) (_yt_player);
  