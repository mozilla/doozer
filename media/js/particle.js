var SAFETY = 10000;
var PI = Math.PI;
var PI_2 = PI/2;
var RAD = PI / 180;

function safe(n) {
    return Math.round(n * SAFETY) / SAFETY;
}
function vmin(a,b) {
    return [a[0]<b[0]?a[0]:b[0],a[1]<b[1]?a[1]:b[1]];
}
function vmax(a,b) {
    return [a[0]>b[0]?a[0]:b[0],a[1]>b[1]?a[1]:b[1]];
}
function vdot(a,b) {
    return a[0]*b[0] + a[1]*b[1];
}
function vcross(a, b) {
    return a[0]*b[1] - b[0]*a[1];
}
function vplus(a, b) {
    return [a[0]+b[0], a[1]+b[1]];
}
function vminus(a, b) {
    return [a[0]-b[0], a[1]-b[1]];
}
function vtimes(a, s) {
    return [a[0]*s, a[1]*s];
}
function vnorm(a) {
    return vunit([a[1], -a[0]]);
}
function vdiv(a, s) {
    return [a[0]/s, a[1]/s];
}
function vsize(a) {
    return Math.sqrt(a[0]*a[0]+a[1]*a[1]);
}
function vunit(a) {
    return vdiv(a, vsize(a));
}
function vsafe(a) {
    return [safe(a[0]), safe(a[1])];
}

function rand(bounds) {
    var range = bounds[1] - bounds[0] + (1 / SAFETY);
    return Math.floor(Math.random() * range * SAFETY) / SAFETY + bounds[0];
}

function now() {
    return (new Date()).getTime();
}

function ParticleEffect(cfg) {
    var stime,
        num = cfg.num || 100,
        particles = [],
        respawn = cfg.respawn || false,
        initNum = cfg.initNum || num,
        interval = false,
        primed = false;
    this.origin = cfg.origin || [0,0];
    this.canvas = cfg.canvas;
    this.ctx = this.canvas.getContext('2d');

    this.addParticle = function (time) {
        var p;
        cfg.particle.origin = this.origin;
        cfg.particle.ctx = this.ctx;
        p = new Particle(cfg.particle);
        particles.push(p);
        p.init(time);
    };
    this.stop = function() {
        respawn = false;
    };
    this.reset = function() {
        particles = [];
        primed = false;
    }
    this.die = function() {
        clearInterval(interval);
    };
    this.init = function() {
        stime = now();
        $(this.canvas).css({
            'position': 'absolute'
        });
        while(particles.length < initNum) {
            this.addParticle(0);
        }
        primed = true;
    };
    this.go = function() {
        respawn = cfg.respawn;
        if (!primed) this.init();
        clearInterval(interval);
        interval = setInterval(this.tick, 50);
    };
    this.tick = function() {
        var elapsed = now() - stime,
            p, i;

        if (respawn && particles.length < num) {
            that.addParticle(elapsed);
        }
        if (particles.length) {
            var min = particles[0].pos,
                max = particles[0].pos;
            for (i=0; i<particles.length; i++) {
                p = particles[i];
                p.tick(elapsed);
                if (p.dead) {
                    if (respawn) {
                        p.o.origin = that.origin;
                        p.init(elapsed);
                    } else {
                        particles.splice(i,1);
                        i--;
                        continue;
                    }
                }

                // find bounds
                min = vmin(min,vminus(p.pos,[p.rad+1, p.rad+1]));
                max = vmax(max,vplus(p.pos,[p.rad+1, p.rad+1]));
            }

            if (particles.length) {
                var size = vminus(max,min);
                size = [Math.ceil(size[0]), Math.ceil(size[1])];
                min = [Math.floor(min[0]), Math.floor(min[1])];
                that.canvas.width = size[0];
                that.canvas.height = size[1];
                that.canvas.style.top = min[1] + "px";
                that.canvas.style.left = min[0] + "px";
                that.ctx.save();
                that.ctx.translate(-min[0],-min[1]);
                for (i=0; i<particles.length; i++) {
                    p = particles[i];
                    p.draw();
                }
                that.ctx.restore();
            }
        }
        if (!particles.length) {
            that.die();
        }
    };
    var that = this;
}

function Particle(cfg) {
    var stime,
        initPos;
    this.vars = {};
    this.o = $.extend({
        init: $.noop,
        tick: $.noop,
        draw: $.noop,
        origin: [0,0],
        life: [1000,2000]
    }, cfg);

    this.init = function(time) {
        this.dead = false;
        this.initPos = this.o.origin;
        this.life = Math.floor(rand(this.o.life));
        this.rad = 2;
        stime = time;

        this.o.init.call(this);
        this.pos = this.initPos;
    };
    this.tick = function(time) {
        this.elapsed = (time - stime);
        this.age = (time - stime) / this.life;
        if (this.age > 1) {
            this.dead = true;
            return;
        }

        this.o.tick.call(this, this.age);
    };
    this.draw = function() {
        this.o.ctx.save();
        this.o.ctx.translate(this.pos[0],this.pos[1]);
        this.o.draw.call(this, this.o.ctx);
        this.o.ctx.restore();
    }
}
