import { Logger, ValidationPipe } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const logger = new Logger();

  app.setGlobalPrefix(`/api/${process.env.SERVICE_NAME}`);

  app.useGlobalPipes(
    new ValidationPipe({
      transform: true,
      whitelist: true,
    }),
  );

  const config = new DocumentBuilder().addBearerAuth().build();
  const documentFactory = () => SwaggerModule.createDocument(app, config);
  SwaggerModule.setup(
    `/api/${process.env.SERVICE_NAME}/docs`,
    app,
    documentFactory,
    {
      jsonDocumentUrl: `/api/${process.env.SERVICE_NAME}/openapi.json`,
    },
  );

  const port = process.env.SERVICE_PORT || 3000;
  await app.listen(port, async () => {
    logger.log(`Server is running on: ${await app.getUrl()}`);
  });
}
bootstrap();
