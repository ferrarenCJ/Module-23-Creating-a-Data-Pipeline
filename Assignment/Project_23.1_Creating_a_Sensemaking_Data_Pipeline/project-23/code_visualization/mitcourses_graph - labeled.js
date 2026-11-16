function graph() {

    // clean up
    document.getElementById('target').innerHTML = '';

    var tip = d3.tip()
        .attr('class', 'd3-tip')
        .html(function(d) {
            return '<span>' + d.word + ': ' + d.score + '</span>';
        })
        .offset([-12, 0]);

    var padding = 6,
        radius = d3.scale.log().range([15, 70]).domain([2, 1278]),
        color = d3.scale.category10();

    var nodes = [];
    var circle = [];
    var force;

    var svg = d3.select("div[id=target]")
        .append("svg")
        .attr("width", 1920)
        .attr("height", 960)
        .attr("class", "vis")
        .append("g");

    svg.call(tip);

    // USE ALL WORDS
    for (var word in scores) {

        nodes.push({
            radius: radius(scores[word]),
            color: color(word.length),
            word: word,
            score: scores[word]
        });

    }

    force = d3.layout.force()
        .nodes(nodes)
        .size([1400, 800])
        .gravity(0.01)
        .charge(-0.01)
        .on("tick", tick)
        .start();

    // freeze layout after 5 seconds
    setTimeout(function () {
        force.stop();
    }, 5000);

    circle = svg.selectAll("circle")
        .data(nodes)
        .enter()
        .append("circle")
        .attr("r", function(d) {
            return d.radius;
        })
        .style("fill", function(d) {
            return d.color;
        })
        .on('mouseover', tip.show)
        .on('mouseout', tip.hide)
        .call(force.drag);

    // word labels
    var wordLabels = svg.selectAll(".wordLabel")
        .data(nodes)
        .enter()
        .append("text")
        .attr("class", "wordLabel")
        .text(function(d) {
            return d.word;
        })
        .attr("text-anchor", "middle")
        .attr("fill", "white")
        .style("font-weight", "bold")
        .style("pointer-events", "none")
        .attr("font-size", function(d) {
            return Math.max(8, d.radius / 4);
        });

    // count labels
    var countLabels = svg.selectAll(".countLabel")
        .data(nodes)
        .enter()
        .append("text")
        .attr("class", "countLabel")
        .text(function(d) {
            return d.score;
        })
        .attr("text-anchor", "middle")
        .attr("fill", "white")
        .style("pointer-events", "none")
        .attr("font-size", function(d) {
            return Math.max(7, d.radius / 5);
        });

    function tick(e) {

        circle
            .each(cluster(10 * e.alpha * e.alpha))
            .each(collide(.5))
            .attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; });

        wordLabels
            .attr("x", function(d) { return d.x; })
            .attr("y", function(d) { return d.y - 5; });

        countLabels
            .attr("x", function(d) { return d.x; })
            .attr("y", function(d) { return d.y + 10; });
    }

    // Move d to be adjacent to the cluster node.
    function cluster(alpha) {

        var max = {};

        nodes.forEach(function(d) {

            if (!(d.color in max) || (d.radius > max[d.color].radius)) {
                max[d.color] = d;
            }

        });

        return function(d) {

            var node = max[d.color],
                l,
                r,
                x,
                y;

            if (node == d) return;

            x = d.x - node.x;
            y = d.y - node.y;
            l = Math.sqrt(x * x + y * y);
            r = d.radius + node.radius;

            if (l != r) {

                l = (l - r) / l * alpha;

                d.x -= x *= l;
                d.y -= y *= l;

                node.x += x;
                node.y += y;

            }
        };
    }

    // Resolve collisions
    function collide(alpha) {

        var quadtree = d3.geom.quadtree(nodes);

        return function(d) {

            var r = d.radius + radius.domain()[1] + padding,
                nx1 = d.x - r,
                nx2 = d.x + r,
                ny1 = d.y - r,
                ny2 = d.y + r;

            quadtree.visit(function(quad, x1, y1, x2, y2) {

                if (quad.point && (quad.point !== d)) {

                    var x = d.x - quad.point.x,
                        y = d.y - quad.point.y,
                        l = Math.sqrt(x * x + y * y),
                        r = d.radius + quad.point.radius +
                        (d.color !== quad.point.color) * padding;

                    if (l < r) {

                        l = (l - r) / l * alpha;

                        d.x -= x *= l;
                        d.y -= y *= l;

                        quad.point.x += x;
                        quad.point.y += y;
                    }
                }

                return x1 > nx2 ||
                       x2 < nx1 ||
                       y1 > ny2 ||
                       y2 < ny1;
            });
        };
    }
}