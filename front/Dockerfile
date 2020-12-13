FROM node:lts-alpine

WORKDIR /app
COPY . /app

RUN npm install

ENV REACT_APP_BACK_URL=${REACT_APP_BACK_URL}
ENV HOST="0.0.0.0"
ENV PORT="3000"

EXPOSE 3000

ENTRYPOINT ["npm", "run"]
CMD ["start"]