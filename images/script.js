const data = {
  name: "Main Orchestrator",
  children: [
    {
      name: "Static Data Orchestrator",
      children: [
        {
          name: "Macroeconomic Data Agent",
          children: [
            { name: "GDP Trends Sub-Agent" },
            { name: "Trade Indices Sub-Agent" },
            { name: "Currency Volatility Sub-Agent" }
          ]
        },
        {
          name: "Historical Route Performance Agent",
          children: [
            { name: "FFA Historical Data Sub-Agent" },
            { name: "Baltic Index Components Sub-Agent" },
            { name: "Seasonal Patterns Sub-Agent" }
          ]
        },
        {
          name: "Commodity Analysis Agent",
          children: [
            { name: "Iron Ore Trade Trends Sub-Agent" },
            { name: "Coal Trade Trends Sub-Agent" },
            { name: "Mining Output Analysis Sub-Agent" }
          ]
        }
      ]
    },
    {
      name: "Dynamic Data Orchestrator",
      children: [
        {
          name: "Real-Time Vessel Tracking Agent",
          children: [
            { name: "AIS Data Parser" },
            { name: "Vessel Availability Sub-Agent" },
            { name: "Ton-Mile Demand Estimator" }
          ]
        },
        {
          name: "Port Disruption Monitoring Agent",
          children: [
            { name: "Weather Impact Sub-Agent" },
            { name: "Port Congestion Tracker" },
            { name: "Geopolitical Disruption Sub-Agent" }
          ]
        },
        {
          name: "Fuel Price and Cost Agent",
          children: [
            { name: "Fuel Price Analysis Sub-Agent" },
            { name: "Fuel Cost Impact Calculator" }
          ]
        }
      ]
    },
    {
      name: "Forecast Orchestrator",
      children: [
        {
          name: "Time Series Forecasting Agent",
          children: [
            { name: "Static Data Integration Node" },
            { name: "Dynamic Data Integration Node" }
          ]
        },
        {
          name: "Route-Specific Predictions Agent",
          children: [
            { name: "C3 Predictions Sub-Agent" },
            { name: "C5 Predictions Sub-Agent" }
          ]
        },
        {
          name: "Market Volatility Modeller",
          children: [
            { name: "Monte Carlo Volatility Simulator" }
          ]
        }
      ]
    },
    {
      name: "Scenario Orchestrator",
      children: [
        {
          name: "Disruption Scenarios Agent",
          children: [
            { name: "Port Closure Scenarios" },
            { name: "Geopolitical Shock Scenarios" },
            { name: "Vessel Supply Shock Scenarios" }
          ]
        },
        {
          name: "Demand Fluctuation Modeller",
          children: [
            { name: "Commodity Demand Surge Scenarios" },
            { name: "Seasonal Demand Drop Scenarios" }
          ]
        },
        {
          name: "Black Swan Scenario Agent",
          children: [
            { name: "Future Trigger Sub-Agent" },
            { name: "Unforeseen High-Impact Event Generator" }
          ]
        }
      ]
    },
    {
      name: "Insights Orchestrator",
      children: [
        {
          name: "Vessel Allocation Agent",
          children: [
            { name: "Spot vs Contract Decision Sub-Agent" },
            { name: "Vessel Deployment Optimiser" }
          ]
        },
        {
          name: "Contract Optimisation Agent",
          children: [
            { name: "Contract Parsing Sub-Agent" },
            { name: "Laytime Penalty Risk Assessment" }
          ]
        },
        {
          name: "Hedging Strategy Agent",
          children: [
            { name: "FFA Hedge Recommendations Sub-Agent" },
            { name: "Market Opportunity Identification" }
          ]
        }
      ]
    }
  ]
};

// Set up SVG dimensions and radius
const width = 1500;
const height = 1000;
const radius = width / 2.5; // Adjusted radius for a larger layout

const svg = d3
  .select("#radial-tree")
  .attr("viewBox", [-width / 2, -height / 2, width, height])
  .style("font", "13px sans-serif");

const root = d3.hierarchy(data);
const tree = d3.tree().size([2 * Math.PI, radius - 100]);
tree(root);

const links = root.links();
const nodes = root.descendants();

// Draw links
svg
  .append("g")
  .selectAll("path")
  .data(links)
  .join("path")
  .attr(
    "d",
    d3
      .linkRadial()
      .angle((d) => d.x)
      .radius((d) => d.y)
  )
  .attr("fill", "none")
  .attr("stroke", "#ccc")
  .attr("stroke-width", 1.5);

// Draw nodes
const node = svg
  .append("g")
  .selectAll("g")
  .data(nodes)
  .join("g")
  .attr(
    "transform",
    (d) =>
      `translate(${Math.cos(d.x - Math.PI / 2) * d.y}, ${
        Math.sin(d.x - Math.PI / 2) * d.y
      })`
  );

// Draw circles at nodes
node
  .append("circle")
  .attr("r", 6)
  .attr("fill", "#69b3a2")
  .attr("stroke", "black")
  .attr("stroke-width", 1.5);

// Add horizontal labels next to nodes
node
  .append("text")
  .attr("dy", "0.31em")
  .attr("x", (d) => (d.x < Math.PI ? 8 : -8)) // Position labels slightly away from the node
  .attr("text-anchor", (d) => (d.x < Math.PI ? "start" : "end")) // Adjust text anchor
  .text((d) => d.data.name)
  .style("font-size", "14px")
  .attr("transform", "translate(0, 0)"); // Keep text aligned to the node
