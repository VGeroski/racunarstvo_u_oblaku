FROM node:18.10.0 as builder
RUN mkdir -p /app
WORKDIR /app
COPY . .
RUN npm install
ENV PATH="./node_modules/.bin:$PATH"
RUN ng build

FROM nginx:alpine
COPY src/nginx/etc/conf.d/default.conf /etc/nginx/nginx.conf
COPY --from=builder /app/dist/front-app usr/share/nginx/html