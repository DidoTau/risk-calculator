# Use a Node.js runtime as the base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application to the container
COPY . .

# Build the Vue.js application
RUN npm run build

# Expose the port that the application is running on
EXPOSE 8080

# Start the application when the container starts
CMD [ "npm", "run", "serve" ]